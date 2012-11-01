#!/usr/bin/env python

# Cho 100 cai bong den
bulb_states = [True for i in range(101)]

"""
Nguoi thu 1 bat het 100 cai len
Nguoi thu 2 tat cai so 2,4,6,8...
Nguoi thu 3 thay doi trang thai bong 3,6,9...
...
Nguoi thu 100 thay doi bong 100
Hoi trang thai sau cung, cac bong nao dang bat?
"""

for i, item in enumerate(bulb_states):
    if i == 0 or i == 1: continue
    for j in range(i, 101, i):
        # Thay doi trang thai
        bulb_states[j] = False if bulb_states[j] == True else True

for i, item in enumerate(bulb_states):
    if item:
        print i
