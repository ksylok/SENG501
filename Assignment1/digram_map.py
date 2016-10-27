#!/usr/bin/env python
#mapper.py

import string
import sys

prev_word = "" 

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word = word.replace(c,"")
        if prev_word  == "": 
        #    print 'exiting'
            prev_word = word
            break 
        #di_gram = (prev_word, word)
        print'%s %s' %(prev_word,word)
        prev_word = word 
