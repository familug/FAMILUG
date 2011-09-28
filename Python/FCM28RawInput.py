#!usr/bin/env python

name = raw_input("Full name: ")
if name == 'Nguyen Viet Hung':
	print 'Hi HVN'
namelist = name.split(' ')
for w in namelist:
	print w,
