#!/usr/bin/env python
#mapper.py

import string
import sys
import os

filepath = os.environ["map_input_file"]
filename = os.path.split(filepath)[-1]

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        print'%s\t%s' %(word, filename)
