#!/usr/bin/python3

from random import choice


# Seventh chords


whole_list = triad_list + seventh_list

# set this to a list of whatever you want to drill on
drill_seq = big_four_list[:]

while drill_seq:
    nxt = choice(drill_seq)
    print("press enter for next chord")
    input()
    print(nxt)
    drill_seq.remove(nxt)
