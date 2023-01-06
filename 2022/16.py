import utils
from itertools import product
import math
import heapq as hq


def parse_input():
    inp = utils.getinput(16).split("\n")[:-1]

    rates = {}
    adj = {}
    for line in inp:
        _, name, _, _, rate, _, _, _, _, *tunnels = line.split(" ")
        rate = int(rate[5:-1])
        tunnels = list(map(lambda s: s.strip(","), tunnels))
        rates[name] = rate
        adj[name] = tunnels
    names = sorted(list(adj.keys()))
    renamer = {name: 1 << inx for inx, name in enumerate(names)}
    assert renamer["AA"] == 1
    adj = {renamer[k]: [renamer[l] for l in v] for k, v in adj.items()}
    rates = {renamer[k]: v for k, v in rates.items()}
    return adj, rates


def part1(data):
    adj, rates = data
    nonzero_valves = sum(x for x, r in rates.items() if r != 0)
    total_cap = sum(rates.values())

    def neigh_gen(state):
        cur_valve, closed_valves, cur_flow = state
        w = total_cap - cur_flow

        # can open current
        if cur_valve & closed_valves:
            yield (cur_valve, closed_valves - cur_valve, cur_flow + rates[cur_valve]), w
        for neigh in adj[cur_valve]:
            yield (neigh, closed_valves, cur_flow), w

    distances = {}
    minutes = {}
    heap = [(0, (1, nonzero_valves, 0), 0)]

    while heap:
        dist, node, mins = hq.heappop(heap)
        if node in distances:
            continue
        if mins == 30 or (not node[1]):
            return total_cap * 30 - dist
        distances[node] = dist
        minutes[node] = mins
        for neighbor, weight in neigh_gen(node):
            if neighbor not in distances:
                hq.heappush(heap, (dist + weight, neighbor, mins+1))


def part2(data):
    adj, rates = data
    nonzero_valves = sum(x for x, r in rates.items() if r != 0)
    total_cap = sum(rates.values())

    def neigh_gen(state):
        cur_valve, closed_valves, cur_flow = state
        w = total_cap - cur_flow

        # can open current
        if cur_valve & closed_valves:
            yield (cur_valve, closed_valves - cur_valve, cur_flow + rates[cur_valve]), w
        for neigh in adj[cur_valve]:
            yield (neigh, closed_valves, cur_flow), w

    # Cartesian product with prevention of same-opening
    def neigh_gen_two(state):
        me_valve, el_valve, closed_valves, cur_flow = state

        for me_neigh, el_neigh in product(neigh_gen((me_valve, closed_valves, cur_flow)),
                                          neigh_gen((el_valve, closed_valves, cur_flow))):
            (me_next, me_closed, me_flow), _ = me_neigh
            (el_next, el_closed, el_flow), w = el_neigh
            if not (me_closed != closed_valves and me_closed == el_closed):
                yield (me_next, el_next, me_closed & el_closed,
                       me_flow + el_flow - cur_flow), w

    distances = {}
    minutes = {}
    heap = [(0, (1, 1, nonzero_valves, 0), 0)]

    max_min = 0
    while heap:
        dist, node, mins = hq.heappop(heap)
        if mins > max_min:
            print(mins, math.log2(len(distances)), math.log2(len(heap)))
            max_min = mins
        if node in distances:
            continue
        if mins >= 26 or (not node[2]):
            return total_cap * 26 - dist
        distances[node] = dist
        minutes[node] = mins
        for neighbor, weight in neigh_gen_two(node):
            if neighbor not in distances:
                hq.heappush(heap, (dist + weight, neighbor, mins+1))


if __name__ == "__main__":
    data = parse_input()
    print("Warning! This takes like 16GB ram and 10+ minutes to run part 2.")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
