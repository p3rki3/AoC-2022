import AoCFramework as AoC

def part_1():   # function to solve part 1 of the problem and return the solution to input to AoC
    priorsum = 0
    for line in Lines:
        for item in line[:int(len(line)/2)]:
            if item in line[int(len(line)/2):]:
                priorsum += ord(item) - 38 if item.isupper() else ord(item) - 96
                break
    return priorsum

def part_2():   # function to solve part 2 of the problem and return the solution to input to AoC
    priorsum = 0
    for count, line in enumerate(Lines):
        if count % 3 == 0:
            for item in line:
                if item in Lines[count+1] and item in Lines[count+2]:
                    priorsum += ord(item) - 38 if item.isupper() else ord(item) - 96
                    break
    return priorsum

Lines = AoC.Init("data/day3.txt")[0]
AoC.run(part_1, part_2)

# verified results are    7742 and 2276
