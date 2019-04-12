/*
 * Name: Chase Kanipe
 * Section: 0102
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Chase Kanipe
 */

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
