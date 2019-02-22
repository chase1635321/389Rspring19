# Writeup 2 - OSINT

Name: Chase Kanipe
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Chase Kanipe

## Assignment Writeup

### Part 1 (45 pts)

1. What is `v0idcache`'s real name?

Elizabeth Moffet. Found this after searching on for v0idcache on Twitter. However, the profile picture is for an actress named Julie Benz.

2. Where does `v0idcache` work? What is the URL to their website?

She is a banking CEO at 1337bank

1446bank.money

This was found on her Twitter.

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.

https://twitter.com/v0idcache
She follows UMD Cybersecurity

Known connection to f1inch

Kown connection to @CacheDev0id

v0idcache@protonmail.com (On her website)

This pastebin, found with google.

```
[+] fl1nch joined
[+] v0idcache joined
[v0idcache] u there?
[fl1nch] hi
[v0idcache] what time are we doing this
[v0idcache] i have a meeting with the board of directors and they're not going to like this
[fl1nch] 1400
[v0idcache] ugh i have to get a flight out of here asap
[fl1nch] lol
[fl1nch] you worry too much
[v0idcache] u would too if you were in as much trouble as i am
[v0idcache] whats the file you need called
[fl1nch] AB4300.txt
[fl1nch] thx - we owe you
[v0idcache] thank me later
[-] v0idcache left
[-] fl1nch left
```

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

142.93.136.81

By searching for the ip location with IP2Location, I found it is in Noord-Holland Amsterdam Netherlands (52.3740 by 4.8897).

The ISP is DigitalOcean LLC.

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.

In /secret_directory from robots.txt
CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

In home page source
CMSC389R-{h1dd3n_1n_plain_5ight}

6. What ports are open on the website? What services are running behind these ports? How did you discover this?

Using nmap -sV <ip address>

```
PORT    STATE    SERVICE      VERSION
22/tcp  open     ssh          OpenSSH 7.6p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp  open     http         Werkzeug httpd 0.14.1 (Python 3.7.2)
135/tcp filtered msrpc
139/tcp filtered netbios-ssn
445/tcp filtered microsoft-ds
1137/tcp open
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

7. Which operating system is running on the website? How did you discover this?

Using nmap -O <ip address>

```
Aggressive OS guesses: Linux 3.12 (93%), Linux 2.6.35 (91%), Linux 3.10 (91%), Linux 2.6.32 (90%), Tandberg VCS video conferencing system (90%), Linux 3.11 - 4.1 (90%), Linux 3.5 (90%), Synology DiskStation Manager 5.1 (90%), Linux 3.1 - 3.2 (89%), Linux 2.6.32 or 3.10 (89%)
```

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)

Found after brute forcing port 1337
CMSC389R-{brut3_f0rce_m4ster}

After moving to the home/files directory. Cat AB4300.txt from the pastebin.
CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}



### Part 2 (75 pts)

I edited the givcen code to attempt all the passwords in the rockyou.txt. I knew it should target port 1337 after attempting a login with netcat. Once the password was found the user could exit the program. There is a shorter rockyou.txt in this directory, but I used the real one for the initial bruteforce to obtain a password of linkinpark. The flags I found are above.
