import AoCFramework as AoC

def part_1(count):   # function to solve part 1 of the problem and return the solution to input to AoC
    for i in range(len(Lines[0])-count):
        if len(set(Lines[0][i:i+count])) == count:
            return i+count

Lines = AoC.Init("data/day6.txt")[0]
AoC.run(part_1(4), part_1(14))

# Verified answers were   1920   and   2334
