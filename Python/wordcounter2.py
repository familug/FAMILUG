#!/usr/bin/env python
import sys

class WordData():
	"""Class for creating object contain counter 
	and happend line numbers of a word"""
	def __init__(self, word, line):
		self.counter = 1
		self.word = word
		self.happened_lines = [line]

	def __repr__(self):
		lines = " ".join(str(line) for line in self.happened_lines)
		return str(self.counter) + " " + self.word + " " + lines

	def increase_counter(self):
		self.counter += 1

	def add_happened_line(self, line):
		if line not in self.happened_lines:
			self.happened_lines.append(line)

def count_words(filename):
	fin = open(filename, 'r')
	lines = fin.readlines()

	d = {}
	#count word and line
	for (number, line) in enumerate(lines):
		#get line number
		line_number = number + 1
		for w in line.split():
			#Lower case
			lower = w.lower()
			if lower in d:
				d[lower].increase_counter()
				d[lower].add_happened_line(line_number)
			else:
				d[lower] = WordData(lower, line_number)

	datas = d.values()
	#sort desc by counter, then asc by word
	datas.sort(key=lambda wdata : (-wdata.counter, wdata.word))
	
	#print out
	for data in datas:
		print data

def main():
	if len(sys.argv) != 2:
		print 'Use: python wordcounter.py word.in'
		sys.exit(1)

	filename = sys.argv[1]
	count_words(filename)

if __name__ == '__main__':
	main()
