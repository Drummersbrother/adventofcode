import utils
import string
from copy import deepcopy


def run():
    inp = utils.getinput(5).split("\n")[:-1]
    n_crate_lines = -1
    n_stacks = -1
    for inx, l in enumerate(inp):
        if l.startswith(" 1"):
            n_crate_lines = inx
            n_stacks = int([x for x in l.split(" ") if x][-1])
            break
    cratelines = inp[:n_crate_lines]
    stacks = [[] for _ in range(n_stacks)]

    for crateline in cratelines[::-1]:
        crateentries = [crateline[i+1] for i in range(0, len(crateline), 4)]
        for stackinx, crateentry in enumerate(crateentries):
            if crateentry == " ": continue
            stacks[stackinx].append(crateentry)
    orig_stacks = deepcopy(stacks)

    for moveline in inp[n_crate_lines+2:]:
        moveline = moveline.split(" ")
        n_mov, src, dst = (int(moveline[i]) for i in (1, 3, 5))
        src -= 1
        dst -= 1

        crates = stacks[src][-n_mov:][::-1]
        stacks[src] = stacks[src][:-n_mov]
        stacks[dst].extend(crates)

    print("Part 1:", "".join([l[-1] for l in stacks]))

    stacks = orig_stacks

    for moveline in inp[n_crate_lines+2:]:
        moveline = moveline.split(" ")
        n_mov, src, dst = (int(moveline[i]) for i in (1, 3, 5))
        src -= 1
        dst -= 1

        crates = stacks[src][-n_mov:]
        stacks[src] = stacks[src][:-n_mov]
        stacks[dst].extend(crates)

    print("Part 2:", "".join([l[-1] for l in stacks]))


if __name__ == "__main__":
    run()
