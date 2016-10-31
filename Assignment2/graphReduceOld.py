#!/usr/bin/env python
#graph_red.py

import string
import sys

def print_node(node_id, node_attrs):
    output = node_id + "\t"
    for attrs in node_attrs:
        output = output + str(attrs) + "|"
    print '%s' % output[:-1]

prev_key = ""
prev_node = ""
num_entries = 0
duplicate = False
for line in sys.stdin:
    line = line.rstrip()
    token = line.split()
    node_id = token[0]
    node_attrs = token[1].split("|")
    #print '%s' % node_attrs[2] 
    if prev_key != node_id:
        if duplicate == False and prev_node != "":
            print_node(prev_key, prev_node)

        prev_key = node_id
        prev_node = node_attrs
        duplicate = False
    elif prev_key == node_id:
        duplicate = True        
        # assume second node is always GRAY
        if prev_node[2] == 'BLACK':
            print_node(prev_key, prev_node)
        elif prev_node[2] == 'WHITE':
            if node_attrs[2] == 'GRAY':
                new_node = node_attrs
                new_node[0] = prev_node[0]
                print_node(node_id, new_node)
        elif prev_node[2] == 'GRAY':
            if node_attrs[1] < prev_node[1]:
                new_node = node_attrs
            else:
                new_node = prev_node
            print_node(node_id, new_node)
    
if duplicate == False:
    print_node(node_id, node_attrs)
