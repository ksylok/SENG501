#!/usr/bin/env python
#transpose.py

import string
import sys

for line in sys.stdin:
    line = line.rstrip()
    entries = line.split(",")
    row_index = entries[1]
    col_index = entries[0]
    value = entries[2]
    partition_key = int(value) % 10
    print '%s,%s,%s,%s' % (partition_key,row_index,col_index,value)
    
