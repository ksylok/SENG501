#!/usr/bin/env python
#graph_map.py

import string
import sys

def print_node(node_id, node_attrs):
    output = node_id + "\t"
    for attrs in node_attrs:
        output = output + str(attrs) + "|"
    print '%s' % output[:-1]

target_node = False
for line in sys.stdin:
    line = line.rstrip()
    token = line.split()
    node_id = token[0]
    node_attrs = token[1].split("|")

    if node_attrs[2] == 'BLACK' or node_attrs[2] == 'WHITE':
        print_node(node_id, node_attrs)

    elif node_attrs[2] == 'GRAY':
        if target_node == False:
            target_node = True
            node_attrs[2] = 'BLACK'
            print_node(node_id, node_attrs)
            # emit child nodes
            adj_list = node_attrs[0].split(",")
            source = int(node_attrs[1]) + 1
            for child_id in adj_list:
                child_attrs = ['NULL', int(node_attrs[1])+1, 'GRAY', node_id]
                print_node(child_id, child_attrs)
        else:
            print_node(node_id, node_attrs)
