import utils
import numpy as np
np.set_printoptions(threshold=int(1e9), linewidth=1000)


def part1():
    inp = utils.getinput(14).split("\n")[:-1]

    paths = []
    for inp_pathdesc in inp:
        paths.append(list(map(lambda s: np.array(tuple(map(int, s.split(","))), dtype=int), inp_pathdesc.split(" -> "))))

    max_coord = np.array((500, 0), dtype=int)
    min_coord = np.array((500, 0), dtype=int)
    for path in paths:
        max_coord = np.max(np.stack([max_coord, *path]), axis=0)
        min_coord = np.min(np.stack([min_coord, *path]), axis=0)

    min_coord[1] -= 1

    field = np.zeros(max_coord-min_coord+4, dtype=int)

    for path in paths:
        for a, b in zip(path, path[1:]):
            l = (np.abs(b-a)).sum()+1
            for coord in np.linspace(a, b, num=l, dtype=int):
                coord -= min_coord
                field[tuple(coord)] = 1

    n_rest = 0
    abyss_height = field.shape[1]-2
    DOWN = [0, -1]
    LEFT = [1, -1]
    RIGHT = [-1, -1]
    while True:
        sand_pos = np.array((500, 0))-min_coord
        abyss = False
        while True:
            if sand_pos[1] == abyss_height:
                abyss = True
                break
            while field[tuple(sand_pos - DOWN)] == 0:
                if sand_pos[1] == abyss_height:
                    abyss = True
                    break
                sand_pos -= DOWN
            if sand_pos[1] == abyss_height:
                abyss = True
                break
            if field[tuple(sand_pos - LEFT)] == 0:
                sand_pos -= LEFT
                continue
            elif field[tuple(sand_pos - RIGHT)] == 0:
                sand_pos -= RIGHT
                continue
            else:
                break
        if abyss: break

        n_rest += 1
        field[tuple(sand_pos)] = 2

    return n_rest


def part2():
    inp = utils.getinput(14).split("\n")[:-1]

    paths = []
    for inp_pathdesc in inp:
        paths.append(list(map(lambda s: np.array(tuple(map(int, s.split(","))), dtype=int), inp_pathdesc.split(" -> "))))
    floor_y = max(map(lambda ps: max(map(lambda p: p[1], ps)), paths))+2
    paths.append((np.array((-2000, floor_y)), np.array((2000, floor_y))))

    max_coord = np.array((500, 0), dtype=int)
    min_coord = np.array((500, 0), dtype=int)
    for path in paths:
        max_coord = np.max(np.stack([max_coord, *path]), axis=0)
        min_coord = np.min(np.stack([min_coord, *path]), axis=0)

    min_coord[1] -= 1

    field = np.zeros(max_coord-min_coord+4, dtype=int)

    for path in paths:
        for a, b in zip(path, path[1:]):
            l = (np.abs(b-a)).sum()+1
            for coord in np.linspace(a, b, num=l, dtype=int):
                coord -= min_coord
                field[tuple(coord)] = 1

    n_rest = 0
    DOWN = [0, -1]
    LEFT = [1, -1]
    RIGHT = [-1, -1]
    while field[tuple(np.array((500, 0))-min_coord)] != 2:
        sand_pos = np.array((500, 0))-min_coord
        while True:
            while field[tuple(sand_pos - DOWN)] == 0:
                sand_pos -= DOWN
            if field[tuple(sand_pos - LEFT)] == 0:
                sand_pos -= LEFT
                continue
            elif field[tuple(sand_pos - RIGHT)] == 0:
                sand_pos -= RIGHT
                continue
            else:
                break

        n_rest += 1
        field[tuple(sand_pos)] = 2

    return n_rest


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
