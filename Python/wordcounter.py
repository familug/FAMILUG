#!/usr/bin/env python
import sys

def nice_print(li):
	for i in li:
		print i[1][0] , i[0] ,
		for num in i[1][1]:
			print num,
		print 

def count_words(filename):
	fin = open(filename, 'r')
	lines = fin.readlines()
	
	words = []
	for line in lines:
		words += line.split()
	
	#Tolower
	words = [w.lower() for w in words]
	
	#remove dup, sort
	removed_dup = sorted(list(set(words)))
	
	d = {}
	for w in removed_dup:
		#first contain cntr, second is lines
		d[w] = [0, []]
	
	#count word and line
	for line in lines:
		line_number = lines.index(line) + 1
		for w in line.split():
			lower = w.lower()
			if lower in removed_dup:
				d[lower][0] += 1
				if line_number not in d[lower][1]:
					d[lower][1].append(line_number)
	
	#sort by desc frequency, then by asc word
	sorted_d = sorted(d.iteritems() , key = lambda x: (x[1][0] * -1, x[0]))
	nice_print(sorted_d)

def main():
    if len(sys.argv) != 2:
        print 'Use: python wx.py word.in'
        sys.exit(1)
 
    filename = sys.argv[1]
    count_words(filename)
 
if __name__ == '__main__':
    main()
