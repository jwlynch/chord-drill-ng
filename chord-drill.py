#!/usr/bin/python3

from random import choice


# Seventh chords

seventh_list = []

maj7s = []
for i in maj_roots:
    maj7s.append(i + "maj7")
seventh_list += maj7s[:]

maj7suss = []
for i in maj_roots:
    maj7suss.append(i + "maj7sus")
    seventh_list += maj7suss[:]

dom7s = []
for i in maj_roots:
    dom7s.append(i + "7")
    seventh_list += dom7s[:]
big_four_list += dom7s[:]

dom7suss = []
for i in maj_roots:
    dom7suss.append(i + "7sus")
seventh_list += dom7suss[:]

min7s = []
for i in maj_roots:
    min7s.append(i + "m7")
seventh_list += min7s[:]
big_four_list += min7s[:]

min7b5s = []
for i in maj_roots:
    min7b5s.append(i + "m7b5")
seventh_list += min7b5s[:]

dim7s = []
for i in maj_roots:
    dim7s.append(i + "dim7")
seventh_list += dim7s[:]

whole_list = triad_list + seventh_list

# set this to a list of whatever you want to drill on
drill_seq = big_four_list[:]

while drill_seq:
    nxt = choice(drill_seq)
    print("press enter for next chord")
    input()
    print(nxt)
    drill_seq.remove(nxt)
