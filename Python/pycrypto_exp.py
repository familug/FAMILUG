#!/usr/bin/env python2

from Crypto.Cipher import AES
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import commands
import random
import base64
import json
from pprint import pprint


KEYLEN = 16


def gen_16_chars_key():
    outfirst = commands.getoutput("date +%N")
    outfirst += commands.getoutput("date +%N")
    return "".join(outfirst[:KEYLEN])


def blockize(plain):
    """
    Pad the plaintext with random number 
    return paddedtext and number of added chars
    """
    cntr = 0
    while len(plain) % KEYLEN != 0:
        cntr += 1
        plain += str(random.randrange(10))

    return (plain, cntr)
    

def encrypt(plain, enkey):
    obj = AES.new(enkey, AES.MODE_ECB)
    # because data must has len = k * keysize
    padded_plain, padded = blockize(plain)
    obj.encrypt(padded_plain)
    return (obj.encrypt(padded_plain), padded)


def aes_decrypt(cypher, enkey, padded):
    obj = AES.new(enkey, AES.MODE_ECB)
    padded_plain = obj.decrypt(cypher)
    plain = "".join(padded_plain[:-padded])
    return plain


def main():
    key = gen_16_chars_key()
    #plain = "hvnsweeting"
    plain = """
    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.
    Do not supply the 'int', 'default', and 'maxwidth' arguments."""

    print "Before trans" , key
    print "Plaintex; " , plain

    cypher, padded = encrypt(plain, key)

    # RSA the key
    private = RSA.generate(1024)
    public = private.publickey()

    pkey = private.exportKey()
    Pkey = public.exportKey()
    #print pkey
    #print Pkey

    #encode base64 convern those bit to char, to dump with json
    encrypted_key = public.encrypt(key, None)
    b64en = base64.b64encode(encrypted_key[0])
    b64_data = base64.b64encode(cypher)
    data = json.dumps({'key': b64en, 'data': b64_data }, indent=4)
    #print encrypted_key
    print "transfering over internet..."
    print "Hahaha, I'm MITM, i'm seeing: ", data

    print "Server received."
    b64en = json.loads(data)['key']
    b64de = base64.b64decode(b64en)
    print "After trans",  
    received_key = private.decrypt(b64de)
    print aes_decrypt(cypher, received_key, padded)
    

    """
    secret_key = os.urandom(16)
    # Padding (see explanations below)
    plaintext_length = (Crypto.Util.number.size(rsa.n) - 2) / 8
    padding = '\xff' + os.urandom(16)
    padding += '\0' * (plaintext_length - len(padding) - len(secret_key))
    """


if __name__ == "__main__":
    main()
