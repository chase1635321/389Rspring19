# Writeup 7 - Binaries I

Name: Chase Kanipe
Section: 0102

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Chase Kanipe

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[]){
	int x8 = 0x1ceb00da;
	int x4 = 0xfeedface;

	printf("%d\n", x4);
	printf("%d\n", x8);

	x4 ^= x8;
	x8 ^= x4;
	x4 ^= x8;

	printf("%d\n", x4);
	printf("%d\n", x8);
}
```

### Part 2 (10 Pts)

This code starts with two hex values as local variables. It then prints both of there values, xors the second with the first, then xors the result with the second, then xors the result with the first. These values are then printed.
