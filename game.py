#!/usr/bin/env python

import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

global stars
stars = 0
global defeated_Boss1
defeated_Boss1 = 0
global defeated_Boss2
defeated_Boss2 = 0

def intro_screen():
    valid = 0
    os.system('clear')
    print "Hello, " + getpass.getuser()
    print "Welcome to ______________!"
    print "To read the instructions, press 'i'."
    print "To begin the game press, 's'."
    while (not valid):
	selectedOption = raw_input('==> ').lower()
        if selectedOption == 'i':
	    return selectedOption
	    valid = 1
    	elif selectedOption == 's':
	    return selectedOption
	    valid = 1
	elif selectedOption == 'quit':
	    exit(0)

def instruction_screen():
    os.system('clear')
    try:
	open("instructions")
	stdin = file("instructions")
    except:
	stderr.write("Error opening instructions\n")
	exit(1)
    for line in stdin:
	print line
    print "Press 'b' to return to the opening screen."
    if raw_input('==> ').lower() == 'b':
        selectedOption = 'b'
    else:
        selectedOption = 'i'
    return selectedOption


def start_game():
    os.system('clear')
    print "****Description of instructions and objectives****"
    while(1):
	choice = raw_input('==> ').lower()
    if choice == 'quit':
        exit(0)
    elif choice == 'e':
	enter_castle()
    else:
         print "That's not an option, try 'e' to enter the castle or 'quit' to end the game.\n"


def start():
    state = 'b'
    while(1):
        if state == 'b':
            state = intro_screen()
        elif state == 'i':
            state = instruction_screen()
        elif state == 's':
            state = start_game()

start()
