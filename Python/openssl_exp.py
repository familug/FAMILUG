#!/usr/bin/env python
# -*- encoding: utf-8
import commands
import random
import json
import os
from pprint import pprint
from tempfile import mkstemp

"""
To generate your own rsa key pair, use below commands:
    openssl genrsa -out hvn.key 2048
Generate pubkey from private key
    openssl rsa -in hvnkey -pubout -out hvn.pub
"""


def main():
    plain = """Well I just want a reason to hope
    A reason to know that I should till be here
    Maybe just a glimpse of the light, a patch of blue sky
    Somthing to believe in
    I just want a reason to hope x2
    Want a reason that I should not let go
    I want a reaon to hope"""

    _, TEMPFILE = mkstemp()

    #data should write to a file because it can contain " and '
    with open(TEMPFILE, "w+") as f:
        f.write(plain)

    # generate random key
    key = commands.getoutput("date +%N")
    # encrypt plaintext with key use AES
    cypher = commands.getoutput("openssl aes-256-cbc -a -in %s -pass pass:%s" % (TEMPFILE, key))
    # remove file
    os.remove(TEMPFILE)
    # encrypt key by RSA
    enkey = commands.getoutput("echo '%s' | openssl rsautl -encrypt -pubin -inkey vpn.pub | openssl base64 -e" % key)

    # Client side
    print "Client sending json data..."
    print 
    jsondata = json.dumps({'data' : cypher, 'key' : enkey}, indent=4)

    # send over internet...
    print "I'm man in the middle, I see : \n", jsondata

    # server side
    print
    print "Here are server size:"
    cmd = "echo '%s' | openssl base64 -d | openssl rsautl -decrypt -inkey vpn.pem" % enkey
    received_key = commands.getoutput(cmd)
    print "We got the key: ", received_key
    print "Decrypting data ..."
    command = "echo '%s' | openssl aes-256-cbc -d -a -pass pass:%s" % (cypher, received_key)
    plaintext = commands.getoutput(command)

    print "Here is plaintext: ", plaintext


if __name__ == "__main__":
    main()
