#! /usr/bin/python3

from random import shuffle

import chords
from chords import sevenths

from chords.common import voicing_objects

# takes a list, shuffles it, then pops the front off

def shufflepick(l):
    result = None

    if len(l) > 0:
        shuffle(l)
        result = l.pop()

    return result

def mk_maj_key(root_list):
    qual_list = ["maj7","m7","m7","maj7","7","m7","m7b5"]
    qual_obj_list = []
    for qual in qual_list:
        qual_obj_list.append(voicing_objects[qual])

    result = list(zip(root_list, qual_obj_list))

    return result

keyC = mk_maj_key(["C","D","E","F","G","A","B"])
keyDb = mk_maj_key(["Db","Eb","F","Gb","Ab","Bb","C"])
keyD = mk_maj_key(["D","E","F","G","A","B","C#"])
keyEb = mk_maj_key(["Eb","F","G","Ab","Bb","C","D"])
keyE = mk_maj_key(["E","F#","G#","A","B","C#","D#"])
keyF = mk_maj_key(["F","G","A","Bb","C","D","E"])
keyFsh = mk_maj_key(["F#","G#","A#","B","C#","D#","E#"])
keyG = mk_maj_key(["G","A","B","C","D","E","F#"])
keyAb = mk_maj_key(["Ab","Bb","C","Db","Eb","F","G"])
keyA = mk_maj_key(["A","B","C#","D","E","F#","G#"])
keyBb = mk_maj_key(["Bb","C","D","Eb","F","G","A"])
keyB = mk_maj_key(["B","C#","D#","E","F#","G#","A#"])

choices = {}

keys = {"C":keyC, "Db":keyDb, "D":keyD, "Eb":keyEb, "E":keyE, "F":keyF, "F#":keyFsh, "G":keyG, "Ab":keyAb, "A":keyA, "Bb":keyBb, "B":keyB}

# in keys.keys, the first keys is my var, the second is Dict.keys()
key_strings = list(keys.keys())
func_dexes = [0,1,2,3,4,5,6]

functions = ["Imaj7","IIm7","IIIm7","IVmaj7","V7","VIm7","VIIm7b5"]
qualities = ["maj7","m7","m7","maj7","7","m7","m7b5"]
