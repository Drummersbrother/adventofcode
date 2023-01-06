import utils
from functools import cmp_to_key


def compare(p1, p2) -> int:
    print(f"In comparison of {p1=} and {p2=}")
    if p1 == p2: return 0
    match p1, p2:
        case (int(v1), int(v2)):
            if v1 < v2:
                return 1
            elif v2 < v1:
                return -1
            else:
                return 0
        case ([v1, *rest1], [v2, *rest2]):
            comp = compare(v1, v2)
            if comp == 0:
                return compare(rest1, rest2)
            else:
                return comp
        case ([], [_, *_]):
            return 1
        case ([_, *_], []):
            return -1
        case (int(a), [*b]):
            return compare([a], b)
        case ([*a], int(b)):
            return compare(a, [b])
        case ([], []):
            return 0


def run():
    inp = utils.getinput(13).split("\n")[:-1]
    inp_pairs = [[]]
    for line in inp:
        if not line.startswith("["):
            inp_pairs.append([])
        else:
            inp_pairs[-1].append(eval(line))

    index_sum = 0

    for inx, (p1, p2) in enumerate(inp_pairs):
        if compare(p1, p2) > 0:
            index_sum += inx+1

    print("Part 1:", index_sum)

    all_packets = [[[2]], [[6]], *[packet for pair in inp_pairs for packet in pair]]
    all_packets = sorted(all_packets, key=cmp_to_key(compare), reverse=True)

    divider_sum = (all_packets.index([[2]])+1)*(all_packets.index([[6]])+1)
    print("Part 2:", divider_sum)


if __name__ == "__main__":
    run()
