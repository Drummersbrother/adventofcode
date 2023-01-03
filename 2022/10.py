import utils
import numpy as np


def run():
    inp = utils.getinput(10).split("\n")[:-1]

    X = 1
    cyc_c = 0

    interesting_cyc_ns = range(20, 240, 40)
    interest_sum = 0

    screen = [" "]*240

    def check_interest(n_cycs):
        nonlocal interest_sum, cyc_c
        for _ in range(n_cycs):
            if (cyc_c+1) in interesting_cyc_ns:
                interest_sum += (cyc_c+1)*X
            if cyc_c < 240:
                if abs((cyc_c % 40)-X) < 2:
                    screen[cyc_c] = "█"
            cyc_c += 1

    for instr, *args in (x.split(" ") for x in inp):
        if instr == "addx":
            check_interest(2)
            X += int(args[0])
        elif instr == "noop":
            check_interest(1)
        else:
            break

    check_interest(max(0, 240-cyc_c))

    print("Part 1:", interest_sum)

    print("Part 2 screen:")
    for i in range(0, 240, 40):
        print(" ".join(screen[i:i+40]))

if __name__ == "__main__":
    run()
