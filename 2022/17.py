import utils
import numpy as np
from itertools import cycle
from tqdm import tqdm
np.set_printoptions(threshold=int(1e9), linewidth=1000)

add_tup = lambda a, b: tuple(sum(x) for x in zip(a, b))

WIND_L, WIND_R = "<>"
DIR_R, DIR_L, DIR_U, DIR_D = (np.array(x) for x in ((1, 0), (-1, 0), (0, 1), (0, -1)))
WIND_TO_DIR = {WIND_L: DIR_L, WIND_R: DIR_R}

ROCK_SHAPES = [np.array([np.array(y) for y in x]).T for x in
               [[[1, 1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
                [[1], [1], [1], [1]], [[1, 1], [1, 1]]]]


class Rock(object):
    def __init__(self, created_at: int = 0):
        self.shape = ROCK_SHAPES[created_at % 5]
        self.w, self.h = self.shape.shape
        self.hor_pos = 2

    @property
    def lines(self):
        return self.lines_at_hor_pos(self.hor_pos)

    def lines_at_hor_pos(self, hor_pos):
        lines = np.zeros((7, self.h))
        lines[hor_pos:hor_pos+self.w, :] = self.shape
        return lines

    def get_wind_moved(self, d: str) -> np.array:
        DIR = WIND_TO_DIR[d]
        hor_pos = self.hor_pos
        if 7-self.w >= hor_pos + DIR[0] >= 0:
            hor_pos += DIR[0]
        return self.lines_at_hor_pos(hor_pos)

    def move_wind(self, d: str):
        DIR = WIND_TO_DIR[d]
        if 7-self.w >= self.hor_pos + DIR[0] >= 0:
            self.hor_pos += DIR[0]
            #print("MOVED!")
            #print(self.lines.T[::-1])


def parse_input():
    inp = utils.getinput(17).split("\n")[:-1][0]
    return list(inp)


def part1(data):
    tot_fall = 2022

    field = np.zeros((7, tot_fall*4 + 15))
    field[:, 0] = 1

    highest_set = 1
    #pprint = lambda a: print((a.T)[::-1])
    wind_dirs = cycle(data)
    for fall_inx in range(tot_fall):
        rock = Rock(fall_inx)
        cur_height = highest_set + 3
        while True:
            d = next(wind_dirs)
            if (field[:, cur_height:cur_height+rock.h] * rock.get_wind_moved(d)).sum() == 0:
                rock.move_wind(d)
                #print("tried move", d)
                #temp_field = field.copy()
                #temp_field[:, cur_height:cur_height+rock.h] += rock.lines
                #pprint(temp_field[:, :cur_height+4])
                #print("--------"*3)
            if (field[:, (cur_height-1):(cur_height-1)+rock.h] * rock.lines).sum() == 0:
                cur_height -= 1
            else:
                field[:, cur_height:cur_height+rock.h] += rock.lines
                break
        highest_set = (field.shape[1] - field.max(axis=0)[::-1].argmax())

    return (field.shape[1] - field.max(axis=0)[::-1].argmax()) - 1


def np_to_tuple(a: np.ndarray):
    return tuple(map(tuple, a))


def part2(data):
    tot_fall = 1000000000000

    jet_len = len(data)
    rock_len = 5
    repeats_by_modmult_to_height = {}
    keep_n = 500
    cut_dist = 100
    field_offset = 0
    field = np.zeros((7, keep_n))
    field[:, 0] = 1

    highest_set = 1
    wind_dirs = cycle(data)
    jet_idx = 0
    fall_inx = 0
    should_jump = True
    while True:
        if fall_inx >= tot_fall: break
        rock = Rock(fall_inx)
        cur_height = highest_set + 3 - field_offset
        fall_dist = 0
        while True:
            d = next(wind_dirs)
            jet_idx += 1
            if (field[:, cur_height:cur_height+rock.h] * rock.get_wind_moved(d)).sum() == 0:
                rock.move_wind(d)
            if (field[:, (cur_height-1):(cur_height-1)+rock.h] * rock.lines).sum() == 0:
                cur_height -= 1
                fall_dist += 1
            else:
                field[:, cur_height:cur_height+rock.h] += rock.lines
                break
        fall_inx += 1

        check_h = 4
        new = field[:, cur_height+rock.h-check_h:cur_height+rock.h]
        highest_here = (field.shape[1] - field.max(axis=0)[::-1].argmax())
        highest_set = field_offset + highest_here
        if should_jump and np.all((np.sum(new, axis=1) > 0)) and (cur_height+rock.h)==highest_here:
            height = highest_set-1
            jet_idx = jet_idx % jet_len
            rock_idx = fall_inx % rock_len
            mod_pair = (jet_idx, rock_idx)
            tnew = np_to_tuple(new)
            if tnew in repeats_by_modmult_to_height:
                if (jet_idx, rock_idx) in repeats_by_modmult_to_height[tnew]:
                    repeats_by_modmult_to_height[tnew][mod_pair].append((fall_inx, height))

                    (f_inx, f_h), (s_inx, s_h) = repeats_by_modmult_to_height[tnew][mod_pair]
                    delta_inx, delta_h = s_inx - f_inx, s_h - f_h
                    n_inx_fits = (tot_fall - fall_inx) // delta_inx

                    fall_inx += n_inx_fits * delta_inx
                    field_offset += n_inx_fits * delta_h
                    highest_set = field_offset + highest_here

                    should_jump = False
                else:
                    repeats_by_modmult_to_height[tnew][mod_pair] = [(fall_inx, height)]
            else:
                repeats_by_modmult_to_height[tnew] = {mod_pair: [(fall_inx, height)]}

        if cur_height > keep_n-cut_dist:
            field_offset += cut_dist
            new_field = np.zeros((7, keep_n))
            new_field[:, :-cut_dist] = field[:, cut_dist:]
            field = new_field

    return highest_set - 1


if __name__ == "__main__":
    data = parse_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
