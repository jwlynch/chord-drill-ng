#! /usr/bin/python3

import chords
from chords import sevenths

from chords.common import voicing_objects

def mk_maj_key(root_list):
    qual_list = ["maj7","m7","m7","maj7","7","m7","m7b5"]
    qual_obj_list = []
    for qual in qual_list:
        qual_obj_list.append(voicing_objects[qual])

    result = list(zip(root_list, qual_obj_list))

    return result

