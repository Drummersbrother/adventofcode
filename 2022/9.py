import utils
import numpy as np


def run():
    inp = utils.getinput(9).split("\n")[:-1]

    dirs = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
    dirs = {k: np.array(v, dtype=int) for k, v in dirs.items()}

    h_pos = np.array((0, 0), dtype=int)
    t_pos = np.array((0, 0), dtype=int)

    visited = {tuple(t_pos)}

    def adjacent(a, b):
        return np.all(np.abs(a-b) < 2)

    def stepdir(h, t):
        # Assumes non-adjacent head and tail
        return np.sign(h-t)

    for move_dir, l in (x.split(" ") for x in inp):
        for _ in range(int(l)):
            h_pos += dirs[move_dir]
            while not adjacent(h_pos, t_pos):
                t_pos += stepdir(h_pos, t_pos)
                visited.add(tuple(t_pos))

    print("Part 1:", len(visited))

    n_knots = 10
    poss = [np.array((0, 0), dtype=int) for _ in range(n_knots)]
    visited = {tuple(poss[n_knots-1])}

    for move_dir, l in (x.split(" ") for x in inp):
        for _ in range(int(l)):
            poss[0] += dirs[move_dir]
            for f_inx in range(1, n_knots):
                l_inx = f_inx - 1
                l_pos, f_pos = poss[l_inx], poss[f_inx]
                while not adjacent(l_pos, f_pos):
                    poss[f_inx] += stepdir(l_pos, f_pos)
                    f_pos = poss[f_inx]
                    if f_inx == n_knots-1:
                        visited.add(tuple(f_pos))

    print("Part 2:", len(visited))


if __name__ == "__main__":
    run()
