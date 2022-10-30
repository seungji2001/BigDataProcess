#!/usr/bin/python3

import sys
datafile = sys.argv[1]
resultfile = sys.argv[2]
movieInfo_d = dict()

with open(datafile,'r') as df:
	for line in df:
		movieInfo = line.split('::')
		movieInfo_c = movieInfo[2].split('|')
		for a in movieInfo_c:
			if a.endswith('\n') == True:
				a = a[:-2]
			if a not in movieInfo_d:
				movieInfo_d[a] = 1
			else:
				movieInfo_d[a]+=1
with open(resultfile,'w') as rf:
	for line in movieInfo_d:
		rf.write(line + ' ' + str(movieInfo_d[line]))
		rf.write('\n')
