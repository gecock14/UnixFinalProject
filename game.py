#!/usr/bin/env python

import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

global keys
keys = 0
global defeated_Boss1
defeated_Boss1 = 0
global defeated_Boss2
defeated_Boss2 = 0
global inventory
inventory = []


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
    print "Press 'e' to enter the castle."
    while(1):
	choice = raw_input('==> ').lower()
	if choice == 'quit':
            exit(0)
    	elif choice == 'e':
	    enter_castle()
    	else:
            print "That's not an option, try 'e' to enter the castle or 'quit' to end the game.\n"


def enter_castle():
    global keys
    os.system('clear')
    print "****Description of hallway****."
    print "*****There are two doors in front of you. Which do you choose, '1' or '2'?****"
    print "Keys: ",keys
    while(1):
        choice = raw_input('==> ').lower()
        if (choice == 'quit'):
            exit(0)
        elif (choice == '1'):
            werewolf_room()
        elif (choice == '2'):
            vampire_room()
        elif(choice == '3' and keys is 2):
            bigboss_room()
	elif(choice == '3' and keys != 2):
	    print "You must obtain the two keys to open this door."
	    return_main()
	elif(choice == '4'):
	    dungeon_room()
	elif(choice == '5'):
	    kitchen_room()
	elif(choice == '6'):
	    library_room()
	elif(choice == '7'):
	    bedroom_room()


def return_main():
    print "Press 'b' to return to the main hall."
    while(1):
        if(raw_input('==> ').lower() == 'b'):
            enter_castle()


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
