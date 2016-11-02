#!/usr/bin/env python
#graph_red.py

import string
import sys

def print_node(node_id, node_attrs):
    output = node_id + "\t"
    for attrs in node_attrs:
        output = output + str(attrs) + "|"
    print '%s' % output[:-1]

def merge_nodes(child_node, exist_node):
    first_part = exist_node[:1]
    second_part = child_node[1:]
    output_attrs = []
    output_attrs.extend(first_part)
    output_attrs.extend(second_part)
    return output_attrs 

childNode = ""
existingNode = ""
prev_key = ""
num_entries = 0
duplicate = False
resolved = False
final_attrs = [] 
greyNodes = False

for line in sys.stdin:
    line = line.rstrip()
    token = line.split("|")
    node_id = token[0]
    node_attrs = token[-4:]

    if prev_key == "":
        prev_key = node_id
        if node_attrs[2] == 'BLACK':
            print_node(node_id, node_attrs)
            resolved = True
        elif node_attrs[2] == 'WHITE':
            existingNode = node_attrs
            childNode = node_attrs
        continue

    if prev_key != node_id and prev_key != "":
        # print previous node
        if resolved == False:
            final_attrs = merge_nodes(childNode, existingNode)
            print_node(prev_key, final_attrs)

        prev_key = node_id
        num_entries = 0
        resolved = False
        duplicate = False

        if node_attrs[2] == 'BLACK':
            print_node(node_id, node_attrs)
            resolved = True

        elif node_attrs[2] == 'WHITE':
            existingNode = node_attrs
            childNode = node_attrs
        continue

    if prev_key == node_id and resolved == False:
        # non-resolved nodes will always be GRAY
        greyNodes = True

        if duplicate == False:
            childNode = node_attrs
            duplicate = True
        else:
#            # keeping child node w/ shortest source distance
            if node_attrs[1] < childNode[1]:
                childNode = node_attrs

if resolved == False:
    final_attrs = merge_nodes(childNode, existingNode)
    print_node(prev_key, final_attrs)

if greyNodes == True:
    sys.stderr.write('reporter:counter:bfs,greyNodes,1\n')
else:
    sys.stderr.write('reporter:counter:bfs,greyNodes,0\n')
