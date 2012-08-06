#!/usr/bin/python
from random import getrandbits


class Package:
    def __init__(self, to_firewall=True):
        self.to_firewall = to_firewall
        self.log = []

    def append_log(node):
        self.log.append(node)


class Table:
    def __init__(self, name, *args):
        self.name = name
        self.chain = args

    def show(self):
        print self.name
        print "*" * 10
        for c in self.chain:
            print c
        print "*" * 10
        print


PREROUTING = "PREROUTING"
POSTROUTING = "POSTROUTING"
FORWARD = "FORWARD"
INPUT = "INPUT"
OUTPUT = "OUTPUT"


def main():

    print "A packet in comming..."
    p = Package(bool(getrandbits(1)))
    print "Is packet to firewall: ", p.to_firewall

    # Init all table
    mangle_tab = Table('Mangle', PREROUTING, POSTROUTING,
            FORWARD, INPUT, OUTPUT)
    filter_tab = Table('Filter', INPUT, OUTPUT, FORWARD)
    nat_tab = Table('NAT', PREROUTING, POSTROUTING, OUTPUT)
    # TODO: use table objs instead of printing

    print "Mangle - PREROUTING"
    print "NAT - PREROUTING"
    print "ROUTING"
    if p.to_firewall:
        print "Mangle - INPUT"
        print "Filter - INPUT"
        print "Processing....."
        print "ROUTING"
        print "Mangle - OUTPUT"
        print "NAT - OUTPUT"
        print "Filter - OUTPUT"
        print "Mangle - POSTROUTING"
        print "NAT - POSTROUTING"
        print "OUT"
    else:
        print "Mangle - FORWARD"
        print "Filter - FORWARD"
        print "Mangle - POSTROUTING"
        print "NAT - POSTROUTING"
        print "To networkB"


if __name__ == "__main__":
    main()
