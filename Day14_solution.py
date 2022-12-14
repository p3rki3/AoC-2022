from itertools import product
import AoCFramework as AoC

bottom, cavesize = 0, 700
cave = [[0]* cavesize for _ in range(cavesize)]

for rock in [[(int(l[0]), int(l[1])) for ln in line.strip().split(" -> ") 
            for l in [ln.split(",")]] for line in AoC.Init("data/day14.txt")[0]]:
    for curr in range(len(rock) - 1):
        start, end = rock[curr], rock[curr + 1]
        sy, ey = min(start[1], end[1]), max(start[1], end[1]) + 1
        sx, ex = min(start[0], end[0]), max(start[0], end[0]) + 1
        for y, x in product(range(sy, ey), range(sx, ex)):
            cave[y][x] = 1
        bottom = ey - 1 if bottom < ey else bottom

for i in range(cavesize):   # add floor for part 2
    cave[bottom + 2][i] = 1

part_1, part_2, done_p1, done_p2 = 0, 0, False, False
while not done_p2:
    grain = (500, 0)
    while not done_p2:
        if grain[1] + 1 > bottom:
            done_p1 = True
        elif cave[0][500]:
            done_p2 = True
            break
        elif not cave[grain[1] + 1][grain[0]]:
            grain = (grain[0], grain[1] + 1)
        elif not cave[grain[1] + 1][grain[0] - 1]:
            grain = (grain[0] - 1, grain[1] + 1)
        elif not cave[grain[1] + 1][grain[0] + 1]:
            grain = (grain[0] + 1, grain[1] + 1)
        else:
            cave[grain[1]][grain[0]] = 1
            break
    part_1 += 1 if not done_p1 else 0
    part_2 += 1 if not done_p2 else 0

AoC.run(part_1, part_2)
# Verified answers   913    and    30762
