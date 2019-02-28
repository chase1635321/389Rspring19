# Writeup 3 - Operational Security and Social Engineering

Name: Chase Kanipe
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Chase Kanipe

## Assignment Writeup


### Part 1

The easiest method, would be to call her, posing as a representative from her bank, saying her account has been hacked. You could ask her mother's maiden name, the city she was born in, and the name of her first pet as security questions. You could then build a fake website for that account that simulates the password reset features, of the real website. This fake site could log her browser, and you could record account details, including the bank pin, as she enters them.

## Part 2

A first vulnerability is the weak password on the port. This password should be changed to something greater than 8 characters that is not found in a well known wordlist.

A second vulnerability is that the port itself is unfiltered. Access could easily be restricted to a specific ip range, or ssh with rsa keys could be used, or port knocking could be employed.

A third vulnerability is that communication with this server is unencrypted. An attacker on the same local network as Elizabeth or the server could intercept a login attempt with a MITM attack and read the plaintext password.
