import utils

def run():
    guide = [tuple(l.split(" ")) for l in utils.getinput(2).split("\n") if l.strip() != ""]
    winscore = lambda them, me: \
        {-2: 0,
         -1: 6, 
         0: 3, 
         1: 0, 
         2: 6}\
        [(ord(them)-ord("A"))-(ord(me)-ord("X"))]
    choosescore = lambda them, me: (ord(me) - ord("X")) +1
    tot_score = sum(map(lambda p: winscore(*p) + choosescore(*p), guide))
    print("part 1:", tot_score)

    offsetguide = {"X": -1, "Y": 0, "Z": 1}
    rel = lambda c: ord(c)-ord("A")
    computeoffset = lambda them, off: chr((rel(them)+offsetguide[off])%3 + ord("X"))
    offsetguided = [(a, computeoffset(a, b)) for a, b in guide]
    tot_guided_score = tot_score = sum(map(lambda p: winscore(*p) + choosescore(*p), offsetguided))
    print("part 2:", tot_guided_score)
    # A X -> A-1 = C, A C rock scissors we lose



if __name__ == "__main__":
    run()
