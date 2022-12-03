import utils

def run():
    curamount = 0
    maxamount = 0
    carrys = []
    for line in utils.getinput(1).split("\n"):
        try: 
            curamount += int(line)
        except ValueError:
            maxamount = max(maxamount, curamount)
            carrys.append(curamount)
            if len(carrys) > 3:
                carrys = sorted(carrys)[-3:]
            curamount = 0
    print("output 1:", maxamount)
    print("output 2:", sum(carrys))



if __name__ == "__main__":
    run()
