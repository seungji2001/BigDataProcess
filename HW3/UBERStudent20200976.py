#!/usr/bin/python3

import sys
import calendar

inputfile = sys.argv[1]
outputfile=sys.argv[2]

def findweekday(day):
	weekofday=['MON','TUE','WED','THU','FRI','SAT','SUN']
	d = day.split('/')
	dnum = calendar.weekday(int(d[2]),int(d[0]),int(d[1]))
	return weekofday[dnum]

dictionary = dict()
with open(inputfile,'r') as rf:
	totalline=rf.read().splitlines()
	for line in totalline:
		arr = line.split(',')
		regionday = arr[0]+','+findweekday(arr[1])  
		if regionday not in dictionary:	
			vehicles=int(arr[2])
			trips=int(arr[3]) 	
			vehiclestrips=str(vehicles)+','+str(trips)
			dictionary[regionday]=vehiclestrips
		else:
			vehicles+=int(arr[2])
			trips+=int(arr[3])
			vehiclestrips=str(vehicles)+','+str(trips)
			dictionary[regionday]=vehiclestrips

with open(outputfile,'w') as of:
	for line in dictionary:
		of.write(line + ' ' + dictionary[line])
		of.write('\n')
