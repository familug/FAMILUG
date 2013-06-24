#!/usr/bin/env python2

# Example 1, iter over some names
def loop_names():
    names = ["pichu", "pikachu", "raichu"]
    for n in names:
        print n

def name_gener():
    yield "pichu"
    yield "pikachu"
    yield "raichu"

def gener_names():
    for n in name_gener():
        print n

loop_names()
gener_names()

# Example 2, iterate over many numbers

def loop_numbers(n):
    nums = range(n)
    for i in nums:
        print i 

def gener_numbers(n):
    # Python allows to define function inside function
    def num_gener(n):
        c = 0
        while c < n:
            yield c
            c = c + 1

    for i in num_gener(n):
        print i

loop_numbers(5)
gener_numbers(5)

''' Do you see the pattern?
When you create a list, and loop over that list, you may replace it with a generator
Generator just a way to not create list, that helps save you memory, get better
performance. Let remmember this pattern, replace your loop with generator when 
possible!
'''
