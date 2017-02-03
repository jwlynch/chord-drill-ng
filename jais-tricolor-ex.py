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

# initialize stacks cr, cq  and cv to have new copy of the full stacks of 12 items
def init():
    cr = roots[:]
    cq = qualities[:]
    cv = top_voices[:]

