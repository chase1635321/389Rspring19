OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

https://github.com/v0idcache
https://github.com/choward4/389Rspring19


1. What is `v0idcache`'s real name?

Elizabeth Moffet. Found this after searching on for v0idcache on Twitter. However, the profile picture is for an actress named Julie Benz.

2. Where does `v0idcache` work? What is the URL to their website?

She is a banking CEO at 1337bank

1446bank.money

This was found on her Twitter.

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.

https://twitter.com/v0idcache
She follows UMD Cybersecurity

v0idcache@protonmail.com (On her website)

This pastebin

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


4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

142.93.136.81

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.

/secret_directory
Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

CMSC389R-{h1dd3n_1n_plain_5ight} (Main site source)


6. What ports are open on the website? What services are running behind these ports? How did you discover this?

7. Which operating system is running on the server that is hosting the website? How did you discover this?

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.

Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
