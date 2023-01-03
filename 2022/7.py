import utils
from typing import List, Any, Dict


class Dir(object):
    def __init__(self, name: str, subobjs: Dict[str, Any], parent: Any = None):
        self.name = name
        self.subobjs = subobjs
        self.parent = parent
        self.is_file = False
        self.is_dir = True

    def size(self):
        return sum(x.size() for x in self.subobjs.values())

    def is_root(self):
        return self.parent is None

    def level(self):
        return 0 if self.is_root() else self.parent.level() + 1

    def show(self):
        return f"{chr(9)*self.level()} - {self.name} (dir){chr(10) if len(self.subobjs)>0 else ''}{chr(10).join([x.show() for x in self.subobjs.values()])}"


class File(object):
    def __init__(self, name: str, size: int, parent: Any = None):
        self.name = name
        self._size = size
        self.parent = parent
        self.is_file = True
        self.is_dir = False

    def size(self):
        return self._size

    def is_root(self):
        return False

    def level(self):
        return self.parent.level() + 1

    def show(self):
        return f"{chr(9)*self.level()} - {self.name} (file, size={self.size()})"


def run():
    inp = utils.getinput(7).split("$")
    inp = [x.split("\n") for x in inp]
    inp = [[y for y in [x[0][1:], *x[1:]] if y] for x in inp]
    inp = [x for x in inp if x]

    rootobj = Dir("/", {})
    cwd: Dir = None
    for (cmd, *outs) in inp:
        if cmd.startswith("cd "):
            if cmd == "cd /":
                cwd = rootobj
            elif cmd == "cd ..":
                cwd = cwd.parent
            else:
                dst = cmd[3:]
                cwd = cwd.subobjs[dst]
        else:
            assert cmd == "ls"
            for out in outs:
                if out.startswith("dir"):
                    name = out[4:]
                    cwd.subobjs[name] = Dir(name, {}, parent=cwd)
                else:
                    size, name = out.split(" ")
                    size = int(size)
                    cwd.subobjs[name] = File(name, size, parent=cwd)

    print(rootobj.show())

    res_sum = 0
    lim_sum = 100000
    def explore(cur: Dir):
        nonlocal res_sum
        cursize = cur.size()
        if cursize <= lim_sum:
            res_sum += cursize
        for subobj in cur.subobjs.values():
            if subobj.is_dir:
                explore(subobj)

    explore(rootobj)

    print("Part 1:", res_sum)

    need_to_delete = 30000000 - (70000000-rootobj.size())

    smallest_del_size = rootobj.size()

    def explore_del(cur: Dir):
        nonlocal smallest_del_size
        cursize = cur.size()
        if need_to_delete <= cursize <= smallest_del_size:
            smallest_del_size = cursize
        for subobj in cur.subobjs.values():
            if subobj.is_dir:
                explore_del(subobj)

    explore_del(rootobj)

    print("Part 2:", smallest_del_size)

if __name__ == "__main__":
    run()
