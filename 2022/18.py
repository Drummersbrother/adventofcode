import utils
import numpy as np
from skimage.morphology import flood_fill
np.set_printoptions(threshold=int(1e9), linewidth=1000)


def parse_input():
    inp = utils.getinput(18).split("\n")[:-1]
    cubes = []
    for line in inp:
        if not line: break
        cubes.append(np.array(list(map(int, line.split(",")))))
    return np.array(cubes)


def part1(data):
    max_coord, min_coord = np.max(data, axis=0), np.min(data, axis=0)
    expand_by = 2
    max_coord += [expand_by]*3
    min_coord -= [expand_by]*3

    data -= min_coord
    max_coord -= min_coord
    min_coord = np.array([0, 0, 0])

    field = np.zeros(tuple(max_coord), dtype=int)
    for x, y, z in data:
        field[x, y, z] = 1

    area = 0
    area += np.sum(np.abs(field[1:, :, :] - field[:-1, :, :]))
    area += np.sum(np.abs(field[:, 1:, :] - field[:, :-1, :]))
    area += np.sum(np.abs(field[:, :, 1:] - field[:, :, :-1]))

    return area


def part2(data):
    max_coord, min_coord = np.max(data, axis=0), np.min(data, axis=0)
    expand_by = 2
    max_coord += [expand_by]*3
    min_coord -= [expand_by]*3

    data -= min_coord
    max_coord -= min_coord
    min_coord = np.array([0, 0, 0])

    field = np.zeros(tuple(max_coord), dtype=int)
    for x, y, z in data:
        field[x, y, z] = 1

    filled_outside = flood_fill(field, (0, 0, 0), 2, connectivity=1)

    field = np.array((filled_outside < 2), dtype=int)

    area = 0
    area += np.sum(np.abs(field[1:, :, :] - field[:-1, :, :]))
    area += np.sum(np.abs(field[:, 1:, :] - field[:, :-1, :]))
    area += np.sum(np.abs(field[:, :, 1:] - field[:, :, :-1]))

    return area


if __name__ == "__main__":
    data = parse_input()
    print("Part 1:", part1(data))
    data = parse_input()
    print("Part 2:", part2(data))
