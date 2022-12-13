from ast import literal_eval
from functools import cmp_to_key
import AoCFramework as AoC

def comp_pkt(p1, p2):
    if isinstance(p1, list) and isinstance(p2, list):
        for sp1, sp2 in zip(p1, p2):
            if res := comp_pkt(sp1, sp2):
                return res
        return comp_pkt(len(p1), len(p2))
    elif isinstance(p1, list) and isinstance(p2, int):
        return comp_pkt(p1, [p2])
    elif isinstance(p1, int) and isinstance(p2, list):
        return comp_pkt([p1], p2)
    elif isinstance(p1, int) and isinstance(p2, int):
        return 0 if p1 == p2 else ((p1 - p2) // abs(p1 - p2))

def process_file():
    global part_1, part_2
    packets = []
    for count, pkt in enumerate(Lines.split("\n\n"), 1):
        packets += map(literal_eval, pkt.splitlines())
        part_1 += count if comp_pkt(packets[-2], packets[-1]) == -1 else 0
    packets += [[[2]], [[6]]]
    packets.sort(key=cmp_to_key(comp_pkt))
    part_2 = (1 + packets.index([[2]])) * (1 + packets.index([[6]]))

part_1 = part_2 = 0
Lines = AoC.Init("data/day13.txt", nolines=True)
process_file()
AoC.run(part_1, part_2)

# Verified answers are   5350  and  19570