#!/usr/bin/env python
# coding: utf-8
# Author: Nguyen Viet Hung
# Email: hvnsweeting@gmail.com

import sys
import re

p = re.compile("pillar\[.*default\(.*\)")


def normalize(s):
    '''
    Convert double quote to single quote
    '''
    return s.replace('"', "'")


def new2old(s):
    '''
    Convert salt['pillar.get'('key:abc')] to pillar['key:abc']
    since pillar.get default return empty string ''
    '''
    if ',' not in s:
        keys = s.split('(')[1].strip('"').strip(')').strip("'").split(':')
        pillar = 'pillar'
        for i in keys:
            pillar = ''.join([pillar,("['{0}']".format(i))])
        return pillar
    else:
        return s


def old2new(x):
    '''
    Convert pillar[]|default() to salt['pillar.get']('key', default)
    '''
    if 'default' in x:
        keys, default_part = x.split('|')
        keys = keys.split('pillar')[1].strip("'[]").split("']['")
        keys = ':'.join(keys)
        print default_part,
        d = default_part.split('default(')[1].strip(")").strip("'")
        print d
        if d.title() not in ('True', 'False') and not any((
                d.startswith('['), d.startswith('('), d.startswith('{'))):
            d = "'{0}'".format(d)
        return "salt['pillar.get']('{0}', {1})".format(keys, d)
    else:
        return x


def chooser(s):
    if 'salt[' in s and ',' not in s:
        p = re.compile(r"salt\['pillar.get'\]\('.*'\)")
        return p, new2old
    else:
        p = re.compile("pillar\[.*default\(.*\)")
        return p, old2new


def convert(line):
    stripped = line.strip('\n')
    p, func = chooser(stripped)
    found = p.findall(stripped)
    if found:
        for old in found:
            new = func(old)
            changed= stripped.replace(old, new)
            return changed + "\n"
    else:
        return stripped + "\n"

def from_filename(fn):
    with open(fn, 'r') as f:
        data = f.readlines()

    with open(fn, 'w') as f:
        for line in data:
            f.write(convert(line))


#for i in ('{% set encoding = pillar[\'encoding\']|default("en_US.UTF-8") %}',
#        "salt['pillar.get']('encoding')",
#        "{% set encoding = pillar['encoding']|default('en_US.UTF-8') %}",
#        ):
#    print convert(i)


import sys
if __name__ == "__main__":
    from_filename(sys.argv[1])
