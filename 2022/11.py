import utils
from collections import deque
from tqdm import tqdm
from math import lcm


def run():
    inp = utils.getinput(11).split("\n")[:-1]

    monkeys = {}

    for _i in range(0, len(inp), 7):
        monkey_n, starters, op, test, iftrue, iffalse = inp[_i:_i+6]
        monkey_n = int(monkey_n[7:-1])
        starters = list(map(int, starters[18:].split(", ")))
        op = eval(f"lambda old: {op[len('  operation: new = '):]}")
        test = int(test[21:])
        iftrue = int(iftrue[29:])
        iffalse = int(iffalse[30:])
        monkeys[monkey_n] = dict(items=deque(starters), op=op, test_div=test, throw_t=iftrue, throw_f=iffalse, n_inspections=0)

    for round_inx in range(20):
        for monkey_inx in range(len(monkeys)):
            monkey = monkeys[monkey_inx]

            while monkey["items"]:
                item_worry = monkey["items"].popleft()
                item_worry = monkey["op"](item_worry) // 3
                monkey["n_inspections"] += 1
                if item_worry % monkey["test_div"] == 0:
                    monkeys[monkey["throw_t"]]["items"].append(item_worry)
                else:
                    monkeys[monkey["throw_f"]]["items"].append(item_worry)

    inspection_numbers = sorted([x["n_inspections"] for x in monkeys.values()])
    monkey_business = inspection_numbers[-1] * inspection_numbers[-2]
    print("Part 1:", monkey_business)

    monkeys = {}

    for _i in range(0, len(inp), 7):
        monkey_n, starters, op, test, iftrue, iffalse = inp[_i:_i+6]
        monkey_n = int(monkey_n[7:-1])
        starters = list(map(int, starters[18:].split(", ")))
        op = eval(f"lambda old: {op[len('  operation: new = '):]}")
        test = int(test[21:])
        iftrue = int(iftrue[29:])
        iffalse = int(iffalse[30:])
        monkeys[monkey_n] = dict(items=deque(starters), op=op, test_div=test, throw_t=iftrue, throw_f=iffalse, n_inspections=0)

    safe_multiple = lcm(*[m["test_div"] for m in monkeys.values()])

    for round_inx in tqdm(range(10000)):
        for monkey_inx in range(len(monkeys)):
            monkey = monkeys[monkey_inx]

            while monkey["items"]:
                item_worry = monkey["items"].popleft()
                item_worry = monkey["op"](item_worry) % safe_multiple
                monkey["n_inspections"] += 1
                if item_worry % monkey["test_div"] == 0:
                    monkeys[monkey["throw_t"]]["items"].append(item_worry)
                else:
                    monkeys[monkey["throw_f"]]["items"].append(item_worry)

    inspection_numbers = sorted([x["n_inspections"] for x in monkeys.values()])
    monkey_business = inspection_numbers[-1] * inspection_numbers[-2]
    print("Part 2:", monkey_business)

if __name__ == "__main__":
    run()
