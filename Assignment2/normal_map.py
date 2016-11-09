#!/usr/bin/env python
#normal_map.py

import string
import sys

for line in sys.stdin:
    line = line.rstrip()
    items_list = line.split()
    for items in items_list:
        if len(items_list) == 1:
            print '%d,%s,%s' % (int(items)%100, items, 0)
        else:
            for i in range(0, len(items_list)):
                if items_list[i] != items:
                    print '%d,%s,%s' % (int(items)%100, items, items_list[i])
                    # extra line that prints w_j for demoninator count
                    print '%d,%s,%s' % (int(items)%100, items, 0)
