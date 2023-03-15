import utils
import numpy as np
from skimage.morphology import flood_fill
np.set_printoptions(threshold=int(1e9), linewidth=1000)


def parse_input():
    inp = utils.getinput(19).split("\n")[:-1]


def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":
    data = parse_input()
    print("Part 1:", part1(data))
    data = parse_input()
    print("Part 2:", part2(data))
