#!/usr/bin/env python
#normal_red.py

import string
import sys

prev_pair = ""
prev_denom = ""
prev_second = ""
tot_pair_count = 0
denom_item_count = 0
for line in sys.stdin:
    line = line.rstrip()
    line = line.strip()
    tokens = line.split(',')
    #print '%s' % tokens
    first_item = tokens[1]
    second_item = tokens[2]

    # first key assumed to be a denom_item_count value
    if prev_denom == "":
        prev_denom = first_item
        prev_second = second_item
        denom_item_count = 1
        continue

    if second_item == '0':
        if prev_denom != first_item:
            #print 'N(%s,%s) / total(%s) = %d/%d' % (prev_denom, prev_second, prev_denom, tot_pair_count, denom_item_count)
            print 'f(%s,%s) = %f' % (prev_denom, prev_second, float(tot_pair_count)/float(denom_item_count))
            
            prev_denom = first_item
            prev_second = second_item
            denom_item_count = 1

        elif prev_denom == first_item:
            denom_item_count = denom_item_count + 1

    elif second_item != '0':
        if prev_second != second_item:
            if prev_second != '0':
                #print 'N(%s,%s) / total(%s) = %d/%d' % (prev_denom, prev_second, prev_denom, tot_pair_count, denom_item_count)
                #print 'f(w_j, w_i) = %f' % (float(tot_pair_count)/float(denom_item_count))
                print 'f(%s,%s) = %f' % (prev_denom, prev_second, float(tot_pair_count)/float(denom_item_count))
            tot_pair_count = 1
            prev_second = second_item

        elif prev_second == second_item:
            tot_pair_count = tot_pair_count + 1

#print 'N(%s,%s) / total(%s) = %d/%d' % (prev_denom, prev_second, prev_denom, tot_pair_count, denom_item_count)
#print 'f(w_j, w_i) = %f' % (float(tot_pair_count)/float(denom_item_count))
print 'f(%s,%s) = %f' % (prev_denom, prev_second, float(tot_pair_count)/float(denom_item_count))
