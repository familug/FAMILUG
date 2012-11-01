#!/usr/bin/env python

bulb_states = [True for i in range(101)]
for i, item in enumerate(bulb_states):
    if i == 0 or i == 1: continue
    for j in range(i, 101, i):
        bulb_states[j] = False if bulb_states[j] == True else True

for i, item in enumerate(bulb_states):
    if item:
        print i
