import utils
import numpy as np
from tqdm import tqdm
np.set_printoptions(threshold=int(1e9), linewidth=1000)


def parse_input():
    inp = utils.getinput(15).split("\n")[:-1]
    sensor_locs = []
    beacon_locs = []
    for line in inp:
        if not line: break
        _, sx, sy, bx, by = line.split("=")
        sx = int(sx[:-3])
        sy = int(sy[:-24])
        bx = int(bx[:-3])
        by = int(by.strip())
        sensor_locs.append((sx, sy))
        beacon_locs.append((bx, by))

    return sensor_locs, beacon_locs


def mh_dist(a, b):
    return sum(map(lambda p: abs(p[0]-p[1]), zip(a, b)))


def part1(data):
    sensor_locs, beacon_locs = data
    intersect_y = 2000000
    shared_intervals = []

    for sensor, beacon in zip(sensor_locs, beacon_locs):
        d = mh_dist(sensor, beacon)

        y_d = abs(sensor[1]-intersect_y)
        if d < y_d: continue
        shared_d = d-y_d
        interval = (sensor[0]-shared_d, sensor[0]+shared_d)
        shared_intervals.append(interval)

    shared_intervals.sort()

    unioned_intervals = [shared_intervals[0]]
    cur_s, cur_e = unioned_intervals[-1]
    for m_s, m_e in shared_intervals[1:]:
        if m_s > cur_e+1:
            unioned_intervals.append((cur_s, cur_e))
            cur_s, cur_e = m_s, m_e
        elif m_e > cur_e:
            cur_e = m_e
            unioned_intervals[-1] = (cur_s, cur_e)

    l = sum(map(lambda i: (i[1]-i[0])+1, unioned_intervals))

    beacon_xs = {x[0] for x in beacon_locs if x[1] == intersect_y}
    for beacon in beacon_xs:
        for s, e in unioned_intervals:
            if s <= beacon <= e:
                l -= 1

    return l


def part2(data):
    sensor_locs, beacon_locs = data
    ds = list(map(lambda p: mh_dist(*p), zip(*data)))
    lim = 4000000

    def get_impossible_intervals(y_coord):
        shared_intervals = []

        for sensor, d in zip(sensor_locs, ds):
            y_d = abs(sensor[1]-y_coord)
            if d < y_d: continue
            shared_d = d-y_d
            interval = (sensor[0]-shared_d, sensor[0]+shared_d)
            shared_intervals.append(interval)

        shared_intervals.sort()

        unioned_intervals = [shared_intervals[0]]
        cur_s, cur_e = unioned_intervals[-1]
        for m_s, m_e in shared_intervals[1:]:
            if m_s > cur_e+1:
                unioned_intervals.append((cur_s, cur_e))
                cur_s, cur_e = m_s, m_e
            elif m_e > cur_e:
                cur_e = m_e
                unioned_intervals[-1] = (cur_s, cur_e)
        return unioned_intervals

    for y_c in tqdm(range(0, lim+1)):
        u_is = get_impossible_intervals(y_c)
        if len(u_is) > 1:
            print(u_is)
            coord = (u_is[0][1]+1, y_c)
            print(coord)
            return coord[0]*4000000 + coord[1]


if __name__ == "__main__":
    data = parse_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
