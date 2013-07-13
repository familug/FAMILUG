#!/usr/bin/env python2

def arg_test(*args):
    for i, arg in enumerate(args):
        print i, repr(arg)

arg_test("hhoho", 1, "2", [])
