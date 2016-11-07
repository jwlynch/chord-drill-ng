#!/usr/bin/python3

from random import choice

maj_roots = ['C','F','Bb','Eb','Ab','Db','F#','B','E','A','D','G']
aug_roots = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','E','A','D','G']

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

# set this to a list of whatever you want to drill on
drill_seq = sus_triads.copy()

while drill_seq:
    nxt = choice(drill_seq)
    print("press enter for next chord")
    input()
    print(nxt)
    drill_seq.remove(nxt)
