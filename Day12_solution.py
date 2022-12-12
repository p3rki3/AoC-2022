from collections import deque
from itertools import product
import AoCFramework as AoC

def path_search(part):
    S, Q = set(), deque()
    for n, l in product(range(Numlines), range(Lenline)):
        if (part == 1 and Board[n][l] == 0) or (part == 2 and Board[n][l] < 2):
            Q.append(((n, l), 0))
    while Q:
        (n, l), d = Q.popleft()
        if (n, l) in S:
            continue
        S.add((n, l))
        if Lines[n][l] == 'E':
            return d
        for dn, dl in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nn, ll = n + dn, l + dl
            if 0 <= nn < Numlines and 0 <= ll < Lenline and Board[nn][ll] <= 1 + Board[n][l]:
                Q.append(((nn, ll), d + 1))

Lines, Numlines = AoC.Init("data/day12.txt", nolines=False, isnumlist=False, printme=False)
Lenline = len(Lines[0])
Board = [ [ 0 for _i in range(Lenline) ] for _j in range(Numlines) ]
for n, l in product(range(Numlines), range(Lenline)):
    Board[n][l] = 0 if Lines[n][l]=='S' else 1 + ord(Lines[n][l]) - ord('a')
    Board[n][l] = 26 if Lines[n][l]=='E' else Board[n][l]
AoC.run(path_search(1), path_search(2))

#Verified answers are   462  and   451