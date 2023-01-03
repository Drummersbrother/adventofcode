import utils
import numpy as np

np.set_printoptions(threshold=1e9, linewidth=1000)

def run():
    inp = utils.getinput(8).split("\n")[:-1]
    heights = np.array([list(map(int, line)) for line in inp])
    is_vis = np.zeros_like(heights, dtype=bool)
    N, M = heights.shape
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def compute_vis(in_heights):
        temp_vis = np.zeros_like(in_heights, dtype=bool)
        for axis in range(2):
            padding = [[0, 0], [0, 0]]
            padding[axis][0] += 1
            padded = np.pad(in_heights, padding, mode="constant", constant_values=-1)
            acc = np.maximum.accumulate(padded, axis=axis)
            acc = np.diff(acc, 1, axis=axis)
            temp_vis |= (acc > 0)
        return temp_vis

    is_vis |= compute_vis(heights)
    is_vis |= np.flip(compute_vis(np.flip(heights)))
    is_vis = np.array(is_vis, dtype=int)

    print("Part 1:", is_vis.sum())

    def num_viewable_for_line_left(line_heights):
        higher_stack = [] # (inx, val)
        ans_for_line = [0 for _ in line_heights]
        for inx, h in enumerate(line_heights):
            while higher_stack and higher_stack[-1][1] < h:
                higher_stack.pop()
            if higher_stack:
                ans_for_line[inx] = inx - higher_stack[-1][0]
            else:
                ans_for_line[inx] = inx
            higher_stack.append((inx, h))
        return np.array(ans_for_line)

    def views_from_view(heights_view):
        return np.array([num_viewable_for_line_left(line) for line in heights_view])

    viewnumbers = []
    for _inx, view_of_array in enumerate((heights, np.swapaxes(heights, 0, 1))):
        view_of_array = view_of_array.copy()
        vns = []
        vns.append(views_from_view(view_of_array))
        vns.append(views_from_view(view_of_array[..., ::-1])[..., ::-1])
        if _inx == 1:
            vns = [np.swapaxes(x, 0, 1) for x in vns]
        viewnumbers.extend(vns)

    scenic_scores = np.ones_like(heights)
    for viewnumber in viewnumbers:
        scenic_scores *= viewnumber

    print("Part 2:", scenic_scores.max())

if __name__ == "__main__":
    run()
