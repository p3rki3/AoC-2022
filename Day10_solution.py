import AoCFramework as AoC

def part_1():
    global txt
    cycle, sigstr, x = 0, 0, 1
    for ins in inst:
        for i in range(2):
            txt[int(cycle / 40)+1].append("█" if abs((cycle % 40) - x) < 2 else ' ')
            cycle += 1
            sigstr += cycle * x if (cycle + 20) % 40 == 0 else 0
            if ins[0] == "noop":
                break
            elif i==1:
                x += int(ins[1])
    return sigstr

def part_2():
    for x in range(len(txt)):     # part_2 answer is text in the list txt
        print(''.join(txt[x]))
    return "See above..."

txt=[[] for x in range(9)]
inst = [line.split(' ') for line in AoC.Init("data/day10.txt")[0]]
AoC.run(part_1, part_2)

# Verified answers are   14160   and    RJERPEFC