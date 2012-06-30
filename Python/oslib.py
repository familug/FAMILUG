#!/usr/env python
import os
import sys

def print_separator():
	print '-'*15,'*' * 5,'-'*15

print 'Learning Python os library'
print_separator()

print 'Process Working Directory'
print 'Current ' , os.getcwd()
print 'Move up ' , os.pardir
os.chdir(os.pardir)
print 'After move ', os.getcwd()

print_separator()
print 'Filesystem Permissions'
print 'File' , __file__
print 'Exists : ' , os.access(__file__, os.F_OK)
print 'CHMOD: RWE - ', os.access(__file__, os.R_OK), os.access(__file__, os.W_OK), os.access(__file__, os.X_OK)

#DIR
print_separator()
print 'Directory'
dir_name = 'os_dir_test'
print 'Creating', dir_name
os.makedirs(dir_name)

file_name = os.path.join(dir_name, 'foo.txt')
print 'Creating', file_name
f = open(file_name, 'wt')
try:
	f.write('bar')
finally:
	f.close()

print 'Listing' , dir_name
print os.listdir(dir_name)

print 'Cleaning up'
os.unlink(file_name)
os.rmdir(dir_name)


