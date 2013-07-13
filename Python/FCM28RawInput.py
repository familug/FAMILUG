#!usr/bin/env python2

name = raw_input("Full name: ")
if name == 'Nguyen Viet Hung':
	print 'Hi HVN'
namelist = name.split(' ')
for w in namelist:
	print w,
