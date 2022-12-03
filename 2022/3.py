import utils
import string

def run():
    rucksack_lines = utils.getinput(3).split("\n")
    rucksack_lines = [x for x in rucksack_lines if x.strip() != ""]
    prio = lambda c: (ord(c)-ord("A")+27) if c in string.ascii_uppercase else (ord(c)-ord("a")+1)
    s = 0
    for rucksack in rucksack_lines:
        n = len(rucksack)
        k = n//2
        front, back = set(rucksack[:k]), set(rucksack[k:])
        incommon = front & back
        incommon = list(incommon)[0]
        s += prio(incommon)

    print("part 1:", s)

    s = 0
    N = len(rucksack_lines)
    for i in range(0, N, 3):
        a, b, c = rucksack_lines[i:i+3]
        a, b, c = tuple(set(x) for x in (a, b, c))
        s += prio(list((a&b)&c)[0])
    print("part 2:", s)
        

if __name__ == "__main__":
    run()
