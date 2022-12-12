from itertools import product
import AoCFramework as AoC

def do_op(op, val):
    if op[0] == "^":
        return val ** 2
    else:
        return val + op[1] if op[0] == "+" else val * op[1]

def solve(iters):
    monkeys, ops, divrs, edges, factor = [], [], [], [], 1

    for monkey in monkeydata.split("\n\n"):
        lines = monkey.split("\n")
        monkeys.append(list(map(int, lines[1][18:].split(", "))))
        op_str = lines[2][13:]
        param = op_str[12:]
        if op_str.find('+') > 0:
            ops.append(['+', int(param)])
        elif op_str.find('*') > 0:
            op = '^' if param == "old" else '*'
            val = 0 if param == "old" else int(param)
            ops.append([op, val])
        divr, tnum, fnum = int(lines[3][21:]), int(lines[4][29:]), int(lines[5][30:])
        divrs.append(divr)
        edges.append((tnum, fnum))
        factor *= divr

    mbus = [0 for i in range(len(monkeys))]
    for i, j in product(range(iters), range(len(monkeys))):
        for item in monkeys[j]:
            mbus[j] += 1
            new_item = do_op(ops[j], item) // 3 if iters == 20 else do_op(ops[j], item)
            monkeys[edges[j][1 - (new_item % divrs[j] == 0)]].append(new_item % factor)
        monkeys[j] = []
    mbus.sort()
    return mbus[-2] * mbus[-1]

monkeydata = AoC.Init("data/day11.txt", nolines=True)
AoC.run(solve(20), solve(10000))

# Verified answers are 120056   and    21816744824
