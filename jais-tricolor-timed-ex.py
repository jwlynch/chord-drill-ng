#!/usr/bin/python3

import sys
from random import shuffle
from random import choice
import time
from itertools import chain, repeat

import argparse

from chords.common import voicing_objects
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", type=int,
                    help="time in seconds between chords (default 5)",
                    default=5)
args = parser.parse_args()

# chord roots
roots = ["A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab"]

# chord qualities
majtriad = 0
mintriad = 1
dom7th = 2
min7th = 3
cho_qu = [majtriad, mintriad, dom7th, min7th]
qualities = cho_qu * 3

# chord voicing:
# 2ndv means second voice of chord, 3rdv means third voice
# 4nc means 4 note chord
v_r = 0
v_2ndv = 1
v_3rdv = 2
v_4thv_r = 3    # if 3 note chord, take the 1st voice, else 4th voice
v_4thv_2ndv = 4 # if 3 note chord, take the 2nd voice, else 4th voice
v_4thv_3rdv = 5 # if 3 note chord, take the 3rd voice, else 4th voice
tr_topvoice = [v_r, v_2ndv, v_3rdv]
top_voices = tr_topvoice + [v_4thv_r] + tr_topvoice + [v_4thv_2ndv] + tr_topvoice + [v_4thv_3rdv]

# choices holds a dict to hold the "stacks" (each of which is a list)
# cr is chord roots, cq is chord qualities, cv is chord voicings, choices holds the whole thing

choices = {}

# set up choices with the roots, qualities and voicings we want to work with
# (in this case, all of them)
def init_choices(choices, roots, qualities, voicings):
    choices['cr'] = [] + roots
    choices['cv'] = [] + voicings
    choices['cq'] = [] + qualities

# given a root, chord quality (from "big four") and voicing, return a string describing the chord
def format_chord(root_str, qual, voicing):
    root = root_str
    voic = voicing

    qual_str = ""
    if qual == majtriad:
        pass
    elif qual == mintriad:
        qual_str = "m"
    elif qual == dom7th:
        qual_str = "7"
    elif qual == min7th:
        qual_str = "m7"

    voicing_str = ""
    if qual in [dom7th, min7th]:
        if voic == v_r:
            voicing_str = "root on top"
        elif voic == v_2ndv:
            voicing_str = "third on top"
        elif voic == v_3rdv:
            voicing_str = "fifth on top"
        elif voic in [v_4thv_r, v_4thv_2ndv, v_4thv_3rdv]:
            voicing_str = "seventh on top"
    elif qual in [majtriad, mintriad]:
        if voic in [v_r, v_4thv_r]:
            voicing_str = "root on top"
        elif voic in [v_2ndv, v_4thv_2ndv]:
            voicing_str = "third on top"
        elif voic in [v_3rdv, v_4thv_3rdv]:
            voicing_str = "fifth on top"

    return "%s%s %s" % (root, qual_str, voicing_str)

# takes a list, shuffles it, then pops the front off

def shufflepick(l):
    result = None

    if len(l) > 0:
        shuffle(l)
        result = l.pop()

    return result

# choose a chord, return a string describing it

def choose_chord(choices):
    if len(choices['cr']) <= 0:
        print("choice pool is empty")
        result = None
    else:
        # pick a root, quality and voicing
        root = shufflepick(choices['cr'])
        qual = shufflepick(choices['cq'])
        voic = shufflepick(choices['cv'])

        if root == "C#":
            root = choice(["C#","Db"])

        result = format_chord(root, qual, voic)

    return result

# print an arbitrary-sized grid of random chords
# (with random root, random lead note and random quality)
def print_grid(choices, cols, rows, cell_size):
    star_cell = "*" * cell_size
    space_cell = " " * cell_size

    starLine = "*"
    spaceLine = "*"
    chordLine = "*"

    for i in range(cols):
        starLine += star_cell + "*"
        spaceLine += space_cell + "*"

    print(starLine)

    for row in range(rows):
        chordLine = "*"
        for col in range(cols):
            nxt = choose_chord(choices)
            chordLine += nxt.center(cell_size) + "*"

        print(spaceLine)
        print(chordLine)
        print(spaceLine)
        print(starLine)

# mainline: test the chord strings

# find max size of chord strings
max_width = 0
for i in roots:
    max_width = max(max_width, len(i))

max_width += 1 # for the space

max_width += len("seventh on top") # longest voicing string

cell_size = max_width + 4 # two spacees on either side

# how many grids can we do?
numGrids = int(len(roots))

def do_12():
    # initialize the stacks
    init_choices(choices, roots, qualities, top_voices)

    for grid in range(numGrids):
        print()
        print()
        print_grid(choices, 1, 1, cell_size)
        sleep(2)

def do_1():
    print()
    print()
    print_grid(choices, 1, 1, cell_size)
    if len(choices['cr']) == 0:
        init_choices(choices, roots, qualities, top_voices)

init_choices(choices, roots, qualities, top_voices)

while True:
    do_1()
    time.sleep(args.time)
