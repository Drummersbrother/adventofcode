import utils
import string
from copy import deepcopy
from collections import deque, defaultdict


def run():
    inp = utils.getinput(6).split("\n")[0]

    window_sz = 4
    sliding_window = deque([])
    counter = defaultdict(lambda: 0)
    n_excess = 0
    for inx, c in enumerate(inp):
        if len(sliding_window) < window_sz:
            sliding_window.append(c)
            counter[c] += 1
            if counter[c] > 1:
                n_excess += 1
            continue

        if n_excess == 0:
            break

        popped = sliding_window.popleft()
        counter[popped] -= 1
        if counter[popped] > 0:
            n_excess -= 1
        sliding_window.append(c)
        counter[c] += 1
        if counter[c] > 1:
            n_excess += 1

    print("Part 1:", inx)

    window_sz = 14
    sliding_window = deque([])
    counter = defaultdict(lambda: 0)
    n_excess = 0
    for inx, c in enumerate(inp):
        if len(sliding_window) < window_sz:
            sliding_window.append(c)
            counter[c] += 1
            if counter[c] > 1:
                n_excess += 1
            continue

        if n_excess == 0:
            break

        popped = sliding_window.popleft()
        counter[popped] -= 1
        if counter[popped] > 0:
            n_excess -= 1
        sliding_window.append(c)
        counter[c] += 1
        if counter[c] > 1:
            n_excess += 1

    print("Part 2:", inx)


if __name__ == "__main__":
    run()
