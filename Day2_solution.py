import AoCFramework as AoC

strat = []
for line in AoC.Init("data/day2.txt")[0]:
    a, x = line.split(' ')
    strat.append([ord(a)-ord('A'), ord(x)-ord('X')])
part_1 = sum((1 + turn[1] + [3, 6, 0][(turn[1]-turn[0]) % 3] ) for turn in strat)
part_2 = sum(([[3, 1, 2], [1, 2, 3], [2, 3, 1]][turn[1]][turn[0]] + 3 * turn[1]) for turn in strat)
AoC.run(part_1, part_2)

# Verified answers were   13924  and   13448