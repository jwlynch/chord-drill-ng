#!/usr/bin/python3

import sys
from random import shuffle

# chord roots
roots = ["A", "Bb", "B", "C", "C#/Db", "D", "Eb", "E", "F", "F#", "G", "Ab"]

# chord qualities
majtriad = 0
mintriad = 1
dom7th = 2
min7th = 3
cho_qu = [majtriad, mintriad, dom7th, min7th]
qualities = cho_qu * 3

# chord voicing
v_r = 0
v_3 = 1
v_5 = 2
v_7_r = 3
v_7_3 = 4
v_7_5 = 5
tr_topvoice = [v_r, v_3, v_5]
top_voices = tr_topvoice + [v_7_r] + tr_topvoice + [v_7_3] + tr_topvoice + [v_7_5]

# choices holds a dict to hold the "stacks" (each of which is a list)
# cr is chord roots, cq is chord qualities, cv is chord voicings, choices holds the whole thing

choices = {}

# set up choices with the roots, qualities and voicings we want to work with
# (in this case, all of them)
def init_choices(choices, roots, qualities, voicings):
    choices['cr'] = [] + roots
    choices['cv'] = [] + voicings
    choices['cq'] = [] + qualities

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
        elif voic == v_3:
            voicing_str = "third on top"
        elif voic == v_5:
            voicing_str = "fifth on top"
        elif voic in [v_7_r, v_7_3, v_7_5]:
            voicing_str = "seventh on top"
    elif qual in [majtriad, mintriad]:
        if voic in [v_r, v_7_r]:
            voicing_str = "root on top"
        elif voic in [v_3, v_7_3]:
            voicing_str = "third on top"
        elif voic in [v_5, v_7_5]:
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

        result = format_chord(root, qual, voic)

    return result

def print_grid(cols, rows, cell_size):
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
            nxt = choose_chord()
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
numGrids = int(len(roots) / 3)

while True:
    # initialize the stacks
    cr = roots[:]
    cq = qualities[:]
    cv = top_voices[:]

    for grid in range(numGrids):
        input("hit enter for next %s chords:" % str(3))
        print()
        print()
        print_grid(3, 1, cell_size)

