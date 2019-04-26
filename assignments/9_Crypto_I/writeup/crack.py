#!/usr/bin/env python3
import hashlib
import string

def crack():
    hashes = []
    for line in open("hashes.txt", "r"):
        hashes.append(line.strip('\n'))

    passwords = open("passwords.txt", "r").readlines()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            hash = hashlib.sha256((c + p).strip('\n').encode()).hexdigest()
            if hash in hashes:
                print((c + p).strip() + ":" + hash)

crack()
