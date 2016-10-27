#!/usr/bin/env python
#mapper.py

import string
import sys
import os

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
            for char in word:
                first_letter = char
                break
        print'%s\t%s' %(first_letter, word)
