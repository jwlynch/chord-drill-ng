#!/usr/bin/python3

from random import choice

from chords import triads
from chords import sevenths
from chords import common

triad_list = triads.triad_list
seventh_list = sevenths.seventh_list

big_four_list = common.big_four_list

whole_list = triad_list + seventh_list

# set this to a list of whatever you want to drill on
drill_seq = big_four_list[:]

# find max chord name length

max_name_length = 0

for i in drill_seq[:]:
    max_name_length = max(max_name_length, len(i))

# add 2 for either side of name
cell_size = max_name_length + 4 

star_cell  = '*' * cell_size
space_cell = ' ' * cell_size

def print_4x1_grid():
    starLine = "*"
    spaceLine = "*"
    chordLine = "*"
    
    for i in range(4):
        starLine += star_cell + "*"
        spaceLine += space_cell + "*"
     
    print(starLine)
    
    for row in range(1):
        chordLine = "*"
        for col in range(4):
            nxt = choice(drill_seq)
            chordLine += nxt.center(cell_size) + "*"
            drill_seq.remove(nxt)

        print(spaceLine)
        print(chordLine)
        print(spaceLine)
        print(starLine)

    input("hit enter for next 12 chords:")
numGrids = int(len(drill_seq) / 4)

for grid in range(numGrids):
    print()
    print()
    print_4x1_grid()
