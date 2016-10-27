#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        print'%s\t%s' %(word,1)
