import re
n_correct = 0
_lines = []

try:
    while True:
        line = input().strip()
        line = re.split(r"[ :-]", line)
        del line[3]
        line[0], line[1] = int(line[0]), int(line[1])+1
        _lines.append(line)
        c = line[3].count(line[2])
        if c in range(*(line[:2])):
            n_correct += 1
except EOFError:
    pass
print(f"Part 1: {n_correct}")

n_correct = 0
for line in _lines:
    line[1] -= 2
    line[0] -= 1
    a, b = None, None
    try:
        a = line[3][line[0]]
        b = line[3][line[1]]
    except IndexError:
        pass
    if bool(a == line[2]) ^ bool(b == line[2]):
        n_correct += 1

print(f"Part 2: {n_correct}")
