####################################################################################
#
# Advent of Code 2022 Framework (c) Simon Perkins MA FCA FBP Dec 2021 to Dec 2022
#
####################################################################################

import time
import types

prog_start_time = 0

def read_file(filename, isnumlist, printme, nolines): # function to read in the input file with the day's puzzle input
    with open(filename, "r") as fp:
        if nolines:
            Text = fp.read()
            return Text
        Lines = fp.readlines()
        if(isnumlist):
            Lines=[' '.join(line.split()) for line in Lines]   # Useful for removing extra white space in arrays of numbers e.g.
        else:
            Lines=[line.rstrip() for line in Lines]            # Useful for text list
    numlines = len(Lines)
    if printme:
        print("Read in a total of ",numlines,"lines of data.")
        print("First line:", Lines[0])
        print("Last line:", Lines[-1], "\n")
    return Lines, numlines

def Init(filename, isnumlist=False, printme=False, nolines=False):
    global prog_start_time
    print("\n2022 Advent of Code - Framework running...\n")
    prog_start_time = time.perf_counter()
    if filename:
        return read_file(filename, isnumlist, printme, nolines)
    else:
        return None, 0

def run(answer1, answer2=None):  # will accept a tuple, or either 1 or 2 answers of fn calls that give answers 
    global prog_start_time
    if type(answer1) == tuple:
        (answer1, answer2) = answer1
    if isinstance(answer1, types.FunctionType):
        print("Part 1 answer is: ", answer1())
    else:
        print("Part 1 answer is: ", answer1)
    prog1_end_time = time.perf_counter()
    print("Elapsed time:", prog1_end_time - prog_start_time, "\n")
    if isinstance(answer2, types.FunctionType):
        print("Part 2 answer is: ", answer2())
    else:
        print("Part 2 answer is: ", answer2)
    prog2_end_time = time.perf_counter()
    print("Elapsed time:", prog2_end_time - prog1_end_time)
    print("Total elapsed time:", prog2_end_time - prog_start_time, "\n")
