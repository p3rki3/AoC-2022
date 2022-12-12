import AoCFramework as AoC
from collections import defaultdict

pathstack, fs = [], defaultdict(int)

def process_file(Lines):
    for line in Lines:
        subline = line.split()
        if subline[0] == "$":           # user entered command coming up...
            if subline[1] == "cd" and subline[2] == "..":   # pop last subdir off the stack
                pathstack.pop()
            elif subline[1] == "ls":    # ignore
                pass
            else:                       # just cd-ed into a new directory, so pop it onto the stack
                pathstack.append(subline[2])
        elif subline[0] != "dir":       # must be output of ls command - ignore any dir listings until we cd there
            for i in range(len(pathstack)):         # add any file sizes onto the filesystem totals for the path
                fs[tuple(pathstack[:i+1])] += int(subline[0])

process_file(AoC.Init("data/day7.txt")[0])
part_1 = sum(dirsize for dirsize in fs.values() if dirsize <= 100000)
part_2 = min(dirsize for dirsize in fs.values() if dirsize >= (fs[("/", )]) - 40000000)
AoC.run(part_1, part_2)

#Verified answers   1845346    and    3636703
