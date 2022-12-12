import AoCFramework as AoC

elfcal, elffood = 0, []
for line in AoC.Init("data/day1.txt")[0]:
    if len(line) > 0:
        elfcal += int(line)
    else:
        elffood.append(elfcal)
        elfcal = 0
elffood.sort()
AoC.run(elffood[-1], sum(elffood[-3:])) 

# Verified answers were  69206  and  197400
