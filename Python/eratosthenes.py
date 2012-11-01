#!/usr/bin/env python

threshold = 101
primes = [True for _ in range(threshold)]

for number in range(len(primes)):
    if number == 0 or number == 1: 
        primes[number] = False
        continue
    for denominator in range(number * 2, threshold, number):
        primes[denominator] = False

for number, isprime in enumerate(primes):
    if isprime:
        print number
