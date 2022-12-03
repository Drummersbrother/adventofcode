import pathlib, os, sys

BASE = (pathlib.Path(__file__).parent).absolute()
INPUTS = BASE / "inputs"

def getinput(day: int):
    with open(INPUTS / f"{day}.txt", mode="r") as inputs_file:
        return inputs_file.read()


