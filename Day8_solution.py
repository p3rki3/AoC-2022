from itertools import product
import AoCFramework as AoC

def is_visible(i, j):
    is_vis1 = is_vis2 = is_vis3 = is_vis4 = 0
    for a in range(0,i):
        if Trees[a][j] >= Trees[i][j]:
            is_vis1 = 1
            break
    for a in range(i+1,len(Trees)):
        if Trees[a][j] >= Trees[i][j]:
            is_vis2 = 1
            break
    for a in range(0,j):
        if Trees[i][a] >= Trees[i][j]:
            is_vis3 = 1
            break
    for a in range(j+1,len(Trees[0])):
        if Trees[i][a] >= Trees[i][j]:
            is_vis4 = 1
            break
    return is_vis1 * is_vis2 * is_vis3 * is_vis4

def score(i,j):
    is_vis1 = is_vis2 = is_vis3 = is_vis4 = 0
    for a in range(i-1,-1,-1):
        is_vis1 += 1
        if Trees[a][j] >= Trees[i][j]:
            break
    for a in range(i+1,len(Trees)):
        is_vis2 += 1
        if Trees[a][j] >= Trees[i][j]:
            break
    for a in range(j-1,-1,-1):
        is_vis3 += 1
        if Trees[i][a] >= Trees[i][j]:
            break
    for a in range(j+1,len(Trees[0])):
        is_vis4 += 1
        if Trees[i][a] >= Trees[i][j]:
            break
    return is_vis1 * is_vis2 * is_vis3 * is_vis4

Trees = [[tree for tree in line] for line in AoC.Init("data/day8.txt",True)[0]]
part1, part2 = len(Trees) * len(Trees[0]), 0
for i, j in product(range(1, len(Trees)-1), range(1, len(Trees[0])-1)):
    part1 -= is_visible(i,j)
    part2 = max(part2, score(i,j))
AoC.run(part1, part2)
# Verified answer   1713   and   268464