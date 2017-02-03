#!/usr/bin/python3

import sys
from random import choice

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

# "global" vars to hold the "stacks"
# cr is chord roots, cq is chord qualities, cv is chord voicings

cr = []
cq = []
tv = []

# choose a chord, return a string describing it

def choose_chord():
    if len(cr) <= 0:
        print("choice pool is empty")
        sys.exit(0)

    # pick a root, quality and voicing
    root = choice(cr)
    qual = choice(cq)
    voic = choice(cv)

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
    #elif qual in [majtriad, mintriad]:

    print("root %s, qual %s, voicing %s" % (root, qual_str, voicing_str))

    return "%s%s %s" % (root, qual_str, voicing_str)

# mainline: test the chord strings

# initialize the stacks
cr = roots[:]
cq = qualities[:]
cv = top_voices[:]

# print out 12 chords
for i in range(12):
    chord = choose_chord()
    print(chord)
