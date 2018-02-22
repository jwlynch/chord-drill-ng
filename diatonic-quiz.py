#! /usr/bin/python3

PY2 = (str is bytes)

if PY2:
    my_input = raw_input
else:
    my_input = input

from random import shuffle,randint

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
keyD = mk_maj_key(["D","E","F#","G","A","B","C#"])
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

allkeys = {"C":keyC, "Db":keyDb, "D":keyD, "Eb":keyEb, "E":keyE, "F":keyF, "F#":keyFsh, "G":keyG, "Ab":keyAb, "A":keyA, "Bb":keyBb, "B":keyB}

# dict comprehension:
# <disi> jim: {k: v for k, v in old_dict.items() if k.meets_some_condition()}

# for now, just as original:
keys = allkeys

# in keys.keys, the first keys is my var, the second is Dict.keys()
key_strings = list(keys.keys())
func_dexes = [0,1,2,3,4,5,6]

choices["keys"] = key_strings[:]
choices["funcDexes"] = func_dexes[:]

functions = ["Imaj7","IIm7","IIIm7","IVmaj7","V7","VIm7","VIIm7b5"]
qualities = ["maj7","m7","m7","maj7","7","m7","m7b5"]

def choose(choices, key_strings, func_dexes, keys):
    choice = {}

    if len(choices["keys"]) == 0:
        choices["keys"] = key_strings[:]

    choice["key"] = shufflepick(choices["keys"])

    if len(choices["funcDexes"]) == 0:
        choices["funcDexes"] = func_dexes[:]

    choice["funcDex"] = shufflepick(choices["funcDexes"])

    key = keys[choice["key"]]

    chord_ref = key[choice["funcDex"]]

    root = chord_ref[0]
    chord_type_obj = chord_ref[1]

    choice["chord"] = root + chord_type_obj.chord_type
    choice["function"] = functions[choice["funcDex"]]

    return choice

def key_question(choice):
    key = choice["key"]
    chord = choice["chord"]
    function = choice["function"]

    prompt = "from which key does the {function} chord {chord} come from?  ".format(key=key, function=function, chord=chord)

    ans = my_input(prompt)

    result = (ans == key)

    return result

def function_question(choice):
    key = choice["key"]
    chord = choice["chord"]
    function = choice["function"]

    print("which function does the {chord} chord serve in the key of {key}? ".format(key=key, function=function, chord=chord))

    choice_letters = ["A","B","C","D","E","F","G"]

    funcDex = functions.index(function)
    choice_letter = choice_letters[funcDex]

    choices = zip(choice_letters, functions)

    for pick in choices:
        print("%s.  %s" % pick)

    ans = my_input("your answer? ")

    result = (ans == function or ans == choice_letter)

    return result

def chord_question(choice):
    key = choice["key"]
    chord = choice["chord"]
    function = choice["function"]

    prompt = "which chord is the {function} in the key of {key}? ".format(key=key, function=function, chord=chord)

    ans = my_input(prompt)

    result = (ans == chord)

    return result

while True:
    which_question = randint(1,3)
    choice = choose(choices, key_strings, func_dexes, keys)

    key = choice["key"]
    chord = choice["chord"]
    function = choice["function"]

    if which_question == 1:
        correct_p = key_question(choice)
        ans = choice["key"]
    elif which_question == 2:
        correct_p = function_question(choice)
        ans = choice["function"]
    else:
        # which_question is 3
        correct_p = chord_question(choice)
        ans = choice["chord"]

    print()

    if correct_p:
        print("That's right!!")
    else:
        print("no, the correct answer was %s." % ans)

    print()
