import AoCFramework as AoC

def move_tail(h, t):
    if abs(h[0] - t[0]) + abs(h[1]-t[1]) >= 3:   # check for diagonal moves first
        t[0] += 1 if h[0] > t[0] else -1
        t[1] += 1 if h[1] > t[1] else -1
    elif abs(h[0] - t[0]) > 1:
        t[0] += 1 if h[0] > t[0] else -1
    elif abs(h[1]-t[1]) > 1:
        t[1] += 1 if h[1] > t[1] else -1
    return t

def rope_simul():
    rope, visited1, visited2 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]], [], []
    dirdict = {'U': [1,0], 'D': [-1,0], 'L': [0,-1], 'R': [0,1]}
    for ins in inst:
        steps = int(ins[1])
        dir = dirdict[ins[0]]
        for step in range(steps):
            rope[0][0], rope[0][1] = rope[0][0] + dir[0], rope[0][1] + dir[1]
            for i in range(9):
                rope[i+1] = move_tail(rope[i],rope[i+1])
            tailpos1 = str(rope[1][0]) + ":" + str(rope[1][1])
            if tailpos1 not in visited1:
                visited1.append(tailpos1)
            tailpos9 = str(rope[9][0]) + ":" + str(rope[9][1])
            if tailpos9 not in visited2:
                visited2.append(tailpos9)
    return len(visited1), len(visited2)

inst = [line.split(' ') for line in AoC.Init("data/day9.txt")[0]]
AoC.run(rope_simul())
#Verified answers are     6018   and    2619