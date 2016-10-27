#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
tot_count = 0
count = 1
for line in sys.stdin:
    digram = line
    #prev_word,word,count = line.split('\t')
    if prev_key==None:
        prev_key=digram
        tot_count=count
        continue
    if prev_key==digram:
        tot_count = tot_count+1
        continue
    if prev_key!=digram:
        print '%s %s' %(prev_key,tot_count)
        prev_key=digram
        tot_count=count
print '%s %s' %(prev_key,tot_count)
