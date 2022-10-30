#!/usr/bin/python3

import sys
import calendar

inputfile = sys.argv[1]
outputfile = sys.argv[2]

def findDay(d):
	year = d[2]
	month = d[0]
	date = d[1]
	day = calendar.weekday(int(year), int(month), int(date))
	
	return day
	

def makeValues(line,v,t):
	a = line.split(',')
	v += a[0]
	t += a[1]
	r = str(v) + ',' + str(t)
	return r

dayofweek=['MON','TUE','WED','THU','FRI','SAT','SUN']
diction=dict()
with open(inputfile,'r') as fp:
	for line in fp:
		a = line[:-2]
		arr1 = a.split(',')
		d = arr1[1].split('/')
		day = findDay(d)
		line_key = arr1[0]+','+dayofweek[day]	
		vehicles=arr1[2]
		trips=arr1[3]
		if line_key in diction:
			diction[line_key]=makeValues(diction[line_key],vehicles,trips)
		else:
			diction[line_key]=str(vehicles) +','+str(trips)
	list(diction.keys()).sort()		
with open(outputfile,'w') as of:
	for line in diction:
		of.write(line + ' ' + diction[line])
		of.write('\n')
