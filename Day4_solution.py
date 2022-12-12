import AoCFramework as AoC

part_1, (Lines, part_2) = 0, AoC.Init("data/day4.txt")
for r in [[int(s) for s in line.replace('-',',').split(',')] for line in Lines]:
    part_1 += (r[0] <= r[2] and r[1] >= r[3]) or (r[2] <= r[0] and r[3] >= r[1])
    part_2 -= (r[1] < r[2] and r[0] < r[2]) or (r[1] > r[3] and r[0] > r[3])
AoC.run(part_1, part_2)

# Verified answers    584   933
