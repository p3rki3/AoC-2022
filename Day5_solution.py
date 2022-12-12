from itertools import product
import AoCFramework as AoC

def part_1():
    load_stacks()
    for move in moves:
        for _count in range(move[0]):
            stacks[move[2]-1].append(stacks[move[1]-1].pop())
    answer = []
    for i in range(len(stacks)):
       answer.append(stacks[i].pop())
    return ''.join(answer)

def part_2():
    load_stacks()
    for move in moves:
        moveme = []
        for _count in range(move[0]):
            moveme.append(stacks[move[1]-1].pop())
        for _count in range(move[0]):
            stacks[move[2]-1].append(moveme.pop())
    answer = []
    for i in range(len(stacks)):
       answer.append(stacks[i].pop())
    return ''.join(answer)

def load_stacks():
    global stacks
    stacks = [[],[],[],[],[],[],[],[],[]]
    for i, j in product(range(8), range(9)):
        try:
            if Lines[7-i][j*4] == '[':
                stacks[j].append(Lines[7-i][1+j*4])
        except IndexError:
            pass

def process_file():
    global moves
    for i in range(Numlines - 10):
        parts = Lines[i+10].split(' ')
        moves.append([int(parts[1]), int(parts[3]), int(parts[5])])

stacks, moves = [], []
Lines, Numlines = AoC.Init("data/day5.txt")
process_file()
load_stacks()
AoC.run(part_1, part_2)

# Verified answers are   MQSHJMWNH    and    LLWJRBHVZ