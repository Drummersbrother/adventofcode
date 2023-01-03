import utils
import string


def run():
    inp = utils.getinput(4).split("\n")[:-1]
    interval_pairs = []
    for line in inp:
        interval_pairs.append(tuple((tuple(map(int, inte.split("-")))) for inte in line.split(",")))

    def firstinsecond(a, b):
        return a[0] <= b[0] and a[1] >= b[1]

    def eithercontained(p):
        a, b = p
        return firstinsecond(a, b) or firstinsecond(b, a)

    print("Part 1:", sum(map(eithercontained, interval_pairs)))

    def overlaps(p):
        a, b = p
        if a[1] >= b[0]:
            return a[0] <= b[1]
        return False

    print("Part 2:", sum(map(overlaps, interval_pairs)))

if __name__ == "__main__":
    run()
