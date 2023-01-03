import utils
import heapq as hq


def run():
    inp = utils.getinput(12).split("\n")[:-1]
    N, M = len(inp), len(inp[0])
    heights = [[0]*M for _ in range(N)]

    start_pos, end_pos = None, None
    zero_coords = []

    for i, line in enumerate(inp):
        for j, c in enumerate(line):
            if c == "S":
                heights[i][j] = ord("a") - ord("a")
                start_pos = (i, j)
            elif c == "E":
                heights[i][j] = ord("z") - ord("a")
                end_pos = (i, j)
            else:
                heights[i][j] = ord(c) - ord("a")
            if heights[i][j] == 0:
                zero_coords.append((i, j))

    def in_range(p):
        return 0 <= p[0] < N and 0 <= p[1] < M

    def gen_dirs(p):
        r, c = p
        for dir in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if in_range(dir): yield dir

    def add_pos(a, b):
        return (a[0]+b[0], a[1]+b[1])

    def neighs_of(p):
        for dir in gen_dirs(p):
            if heights[dir[0]][dir[1]] <= heights[p[0]][p[1]]+1:
                yield dir

    def dijkstra(neigh_gen, start):
        distances = {}
        heap = [(0, start)]

        while heap:
            dist, node = hq.heappop(heap)
            if node in distances:
                continue
            distances[node] = dist
            for neighbor in neigh_gen(node):
                if neighbor not in distances:
                    hq.heappush(heap, (dist + 1, neighbor))

        return distances

    explore_dists = dijkstra(neighs_of, start_pos)
    end_dist = explore_dists[end_pos]

    print("Part 1:", end_dist)

    def inv_neighs_of(p):
        for dir in gen_dirs(p):
            if heights[p[0]][p[1]] <= heights[dir[0]][dir[1]]+1:
                yield dir

    explore_dists_inv = dijkstra(inv_neighs_of, end_pos)

    best_from_0 = end_dist
    for zero_coord in zero_coords:
        best_from_0 = min(best_from_0, explore_dists_inv.get(zero_coord, end_dist))

    print("Part 2:", best_from_0)


if __name__ == "__main__":
    run()
