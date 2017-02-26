#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: hvn@familug.org
# Tested with Python3
# python major_scale.py C
# ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

import argparse

__doc__ = '''Script prints out major scale start from input note.'''

notes = ('A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab')
noteno = len(notes)
WHOLE = 2
HALF = 1


def next_steps(note, steps=HALF):
    idx = notes.index(note)
    for step in range(steps):
        idx = (idx + 1) % noteno
    return notes[idx]


def major_scale(start):
    out = []
    out.append(start)
    n = start
    for step in [WHOLE, WHOLE, HALF, WHOLE, WHOLE, WHOLE, HALF]:
        n = next_steps(n, step)
        out.append(n)

    return out


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument('note', help='Note starts the major scale')
    args = argp.parse_args()
    print(major_scale(args.note))


if __name__ == "__main__":
    main()
