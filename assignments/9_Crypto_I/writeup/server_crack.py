#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    server_ip = "134.209.128.58"
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    for i in range(0, 3):
        data = s.recv(1024)
        hash1 = data.decode().split("\n")[2]
        cracked1 = crack(hash1)
        print(cracked1 + " : " + hash1)
        time.sleep(.1)
        s.send((cracked1 + "\n").encode())
    print(s.recv(1024).decode())


def crack(hash):
    passwords = open("passwords.txt", "r").readlines()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            h = hashlib.sha256((c + p).strip('\n').encode()).hexdigest()
            if h == hash:
                return((c + p).strip())

server_crack()
