numbers = []
try:
    while (x := input()):
        numbers.append(int(x))
except EOFError:
    pass

num_counts = {}
num_inxs = {}

for inx, num in enumerate(numbers):
    if num in num_counts:
        num_counts[num] += 1
    else:
        num_counts[num] = 1
    num_inxs[num] = inx

for num in numbers:
    other_num = 2020-num
    if other_num in num_counts and num != 1010:
        print(num * other_num)
        break
    elif other_num in num_counts:
        if num_counts[other_num] >= 2:
            print(num * other_num)
            break

print("Now part 2:")

for i, a in enumerate(numbers):
    for j, b in enumerate(numbers[i+1:]):
        if num_inxs.get(2020-(a+b), -1) > j:
            print(a*b*(2020-(a+b)))
            exit()

