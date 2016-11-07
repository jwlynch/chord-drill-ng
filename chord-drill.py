#!/usr/bin/python3

from random import choice

maj_roots = ['C','F','Bb','Eb','Ab','Db','F#','B','E','A','D','G']
aug_roots = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','E','A','D','G']

# Triads

maj_triads = maj_roots.copy()

min_triads = []
for i in maj_roots:
    min_triads.append(i + " m")

dim_triads = []
for i in maj_roots:
    dim_triads.append(i + " dim")

aug_triads = []
for i in aug_roots:
    aug_triads.append(i + " aug")

sus_triads = []
for i in maj_roots:
    sus_triads.append(i + " sus")

# Seventh chords

maj7s = []
for i in maj_roots:
    maj7s.append(i + " maj 7")

maj7suss = []
for i in maj_roots:
    maj7suss.append(i + " maj 7 sus")

dom7s = []
for i in maj_roots:
    dom7s.append(i + "7")

dom7suss = []
for i in maj_roots:
    dom7suss.append(i + "7sus")

min7s = []
for i in maj_roots:
    min7s.append(i + " min 7")

min7b5s = []
for i in maj_roots:
    min7b5s.append(i + " min 7b5")

dim7s = []
for i in maj_roots:
    dim7s.append(i + " dim 7")

# set this to a list of whatever you want to drill on
drill_seq = dim7s.copy()

while drill_seq:
    nxt = choice(drill_seq)
    print("press enter for next chord")
    input()
    print(nxt)
    drill_seq.remove(nxt)
