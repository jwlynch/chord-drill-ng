#!/usr/bin/python3

from random import choice

from chords import triads
from chords import sevenths
from chords import common

triad_list = triads.triad_list
seventh_list = sevenths.seventh_list

big_four_list = common.big_four_list

triad_voicing_list = common.triad_voicing_list

whole_list = triad_list + seventh_list

# dom7 and min7
mindom7 = []
mindom7 += sevenths.dom7s[:] + sevenths.min7s[:]

# set this to a list of whatever you want to drill on
drill_seq = big_four_list[:]

while drill_seq:
    nxt = choice(drill_seq)
    print("press enter for next chord")
    input()
    print(nxt)
    drill_seq.remove(nxt)
