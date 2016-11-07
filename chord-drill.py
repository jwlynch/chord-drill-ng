#!/usr/bin/python3

from random import choice

maj_roots = ['C','F','Bb','Eb','Ab','Db','F#','B','E','A','D','G']
aug_roots = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','E','A','D','G']

# Triads

triad_list = []

maj_triads = maj_roots.copy()
triad_list += maj_triads

min_triads = []
for i in maj_roots:
    min_triads.append(i + " m")
triad_list += min_triads

dim_triads = []
for i in maj_roots:
    dim_triads.append(i + " dim")
triad_list += dim_triads

aug_triads = []
for i in aug_roots:
    aug_triads.append(i + " aug")
triad_list += aug_triads

sus_triads = []
for i in maj_roots:
    sus_triads.append(i + " sus")
triad_list += sus_triads

# Seventh chords

seventh_list = []

maj7s = []
for i in maj_roots:
    maj7s.append(i + " maj 7")
seventh_list += maj7s

maj7suss = []
for i in maj_roots:
    maj7suss.append(i + " maj 7 sus")
seventh_list += maj7suss

dom7s = []
for i in maj_roots:
    dom7s.append(i + "7")
seventh_list += dom7s

dom7suss = []
for i in maj_roots:
    dom7suss.append(i + "7sus")
seventh_list += dom7suss

min7s = []
for i in maj_roots:
    min7s.append(i + " min 7")
seventh_list += min7s

min7b5s = []
for i in maj_roots:
    min7b5s.append(i + " min 7b5")
seventh_list += min7b5s

dim7s = []
for i in maj_roots:
    dim7s.append(i + " dim 7")
seventh_list += dim7s

whole_list = triad_list + seventh_list

# set this to a list of whatever you want to drill on
drill_seq = dim7s.copy()

while drill_seq:
    nxt = choice(drill_seq)
    print("press enter for next chord")
    input()
    print(nxt)
    drill_seq.remove(nxt)
