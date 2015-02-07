#!/usr/bin/env python2

# by hvn@familug.org
# Sat Feb  7 09:39:01 ICT 2015
# to see WTF I did last year

'''
./wtfidly.py english 2 spanish -5 french -3 money -2 violin 5 \
        guitar 2 health -3 book 2 fame 1 relation -2 \
        python 1 golang 1 bash 1 career 2
                    0 X                   : golang
                    0 X                   : python
                X X 0                     : money
                    0 X X                 : english
              X X X 0                     : french
                    0 X X                 : guitar
                    0 X X                 : career
                    0 X X                 : book
              X X X 0                     : health
                    0 X                   : bash
          X X X X X 0                     : spanish
                    0 X X X X X           : violin
                    0 X                   : fame
                X X 0                     : relation
'''

import sys


def draw(scores):
    for metric, value in scores.iteritems():
        value = int(value)
        negative = []
        positive = []
        for i in xrange(10):
            if value < 0:
                positive.append(' ')
                negative.append('X' if i < abs(value) else ' ')
            else:
                negative.append(' ')
                positive.append('X' if i < value else ' ')

        negative.reverse()

        print '{0} 0 {1} : {2}'.format(' '.join(negative),
                                       ' '.join(positive),
                                       metric)


def main():
    scores = {}
    args = sys.argv[1:]
    for i, v in enumerate(args):
        if i % 2 == 0:
            scores[v] = args[i+1]
    draw(scores)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print "I'm tired, bye!"
