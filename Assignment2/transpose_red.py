#!/usr/bin/env python
#transpose_red.py

import string
import sys

for line in sys.stdin:
    line = line.rstrip()
    entries = line.split(",")
    print '%s,%s,%s' % (entries[1],entries[2],entries[3])
    
