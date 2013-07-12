#!/usr/bin/env python2
'''
Simple example creates functions and call them on-fly
'''


def create_func(name):
    def print_name():
        print "hello", name
    return print_name

funcs = {i: create_func(i) for i in ('Pichu', 'Pikachu', 'Raichu')}

for fname in funcs:
    print fname
    funcs[fname]()
