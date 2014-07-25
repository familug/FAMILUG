#!/usr/bin/env python
# Author: Hung Nguyen Viet <hvn@familug.org>
# Code for Trello.com job at developer position
# Fri Jul 25 17:50:58 ICT 2014
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
LETTERS = 'acdegilmnoprstuw'


def trello(s):
    h = 7
    letters = LETTERS
    log.debug('letters range: {}'.format(letters))
    for char in s:
        log.debug('hash now is: {1}, processing: {0}'.format(char, h))
        idx = letters.index(char)
        log.debug('index of {0} is {1}'.format(char, idx))
        h = h * 37 + idx
        log.debug(h)
    return h

sample = 'leepadg'
assert trello(sample) == 680131659347


def trello_revert(hash, chars=None):
    if not chars:
        chars = []
    # hash = idx (<=15) will % 37 == 0
    if hash < 37:
        return
    for i in range(0, len(LETTERS)):
        if (hash - i) % 37 == 0:
            log.debug(LETTERS[i])
            chars.insert(0, LETTERS[i])
            trello_revert((hash - i)/37, chars)

    return ''.join(chars)

dest = 910897038977002
log.info(trello_revert(trello(sample)))
log.info(trello_revert(dest))

log.critical('Congratulation, welcome to Trello.com!')
