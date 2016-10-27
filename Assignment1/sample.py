#!/usr/bin/env python
#sample.py

import string
import sys
from random import random

for line in sys.stdin:
    line = line.strip()
    if random() <= 0.1:
        print line 
