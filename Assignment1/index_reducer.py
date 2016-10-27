#!/usr/bin/env python
#index_reducer.py

import string
import sys

prev_key = None
file_list = ""
total_files = []
for line in sys.stdin:
	line = line.rstrip()
	word,filename = line.split('\t')
	if prev_key==None:
		prev_key=word
		file_list = filename
        total_files.append(file_list)
        continue
	if prev_key==word:
		if filename not in file_list:
            file_list = file_list + ',' + filename
            total_files.append(file_list)
        continue
	if prev_key!=word:
		print '%s\t%s' %(prev_key,file_list)
		prev_key=word
		file_list=filename
        total_files.append(file_list)
print '%s\t%s'% (prev_key,total_files)
