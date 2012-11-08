#!/usr/bin/env python

# Cho 100 cai bong den
n = 101
bulb_states = [True for _ in range(n)]
bulb_states[0] = False

"""
Nguoi thu 1 bat het 100 cai len
Nguoi thu 2 tat cai so 2,4,6,8...
Nguoi thu 3 thay doi trang thai bong 3,6,9...
...
Nguoi thu 100 thay doi bong 100
Hoi trang thai sau cung, cac bong nao dang bat?
"""

for number in range(n):
    if number == 0 or number == 1: continue
    for kxnumber in range(number, 101, number):
        # Thay doi trang thai
        bulb_states[kxnumber] = False if bulb_states[kxnumber] == True else True

print "Bulbs are on: ",
for number, is_on in enumerate(bulb_states):
    if is_on:
        print number,
