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


def werewolf_room():
    global inventory
    print "*****Werewolf room descriptions and options****"
    if('item1' not in inventory):
	kicked("No man can face a werewolf bare handed!")
    else:
	use_item("werewolf", "item1")


def vampire_room():
    global inventory
    print "*****Vampire room description and options****"
    if('item2' not in inventory):
        kicked("Your mortal ways cannot harm me!")
    else:
        use_item("vampire", "item2")


def bigboss_room():
    print "*****BIG BOSS room descriptions and options****"
    dodged = 0
    grabbed = 0
    swing = 0
    while(1):
        action = raw_input('==> ').lower()
        if(action == 'dodge' and dodged == 0):
            print "**Pass phase 1**"
            dodged = 1
        elif(action == 'jump'):
            kicked("**Wrong option**")
        elif(action == 'punch'):
            kicked("**wrong option**")
        elif(action == 'grab' and dodged == 1 and grabbed == 0):
            print "**Pass phase 2**"
            grabbed = 1
        elif(action == 'kick'):
            kicked( "**wrong option**")
        elif(action == 'swing' and grabbed == 1):
            print "**Pass Phase 3**"
        elif(action == 'drop' and swing == 0):
            kicked("**wrong option**")
        elif(action == 'throw' and swing == 0):
            print "***Big Boss Dies***"
            end_game()

def end_game():
    print "You Win!"
    while(1):
        print "Press 'm' to go to the main menu"
        if(raw_input('==> ').lower() == 'm'):
            start()


def use_item(boss, item):
    global keys
    keys = keys + 1
    while(1):
	print "Press 'u' to use ", item
	choice = raw_input('==> ')
	if(choice == 'u'):
	    break
	else:
	   continue

    if(boss == "werewolf"):
	print "No not a silver bullet!!"
	print "**The werewolf collapses onto the floor. You take the key from around his neck.**"
    elif(boss == "vampire"):
	print "Noo! Not a wooden stake!"
	print "**The vampire burns up into a pile of ashes with a key in it. You bend down and take the key.**"

def kicked(reason):
    print reason
    return_main()



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

def dungeon_room():
    print ''' Description/instructions'''
    prompt_dungeon_room()

def prompt_dungeon_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
	enter_castle()
    elif prompt == "1":
        print ''' Item 1 specifics '''
	if prompt not in inventory:
	    print '''you now have item 1'''
	    inventory.append(prompt) 
	else:
	    print "No item here"	
	    prompt_dungeon_room()	
    elif prompt == "2":
	print ''' Item 2 specifics '''
    elif prompt == "3":
	print ''' Item 3 specifics '''
    else:
	print "That command was not valid"
	prompt_dungeon_room()	


def kitchen_room():
    global inventory
    print ''' Description/instructions'''
    prompt_kitchen_room()

def prompt_kitchen_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
        enter_castle()
    elif prompt == "1":
        print ''' Item 1 specifics '''
        if prompt not in inventory:
            print '''you now have item 1'''
	    inventory.append(prompt)
    	else:
	    print '''no item here'''
	    prompt_kitchen_room()
    elif prompt == "2":
        print ''' Item 2 specifics '''
    elif prompt == "3":
	print ''' Item 3 specifics '''
    else:
	prompt_kitchen_room()



def bedroom_room():
    global inventory
    print ''' Description/instructions'''
    prompt_bedroom_room()

def prompt_bedroom_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
        enter_castle()
    elif prompt == "1":
        print ''' Item 1 specifics '''
	if prompt not in inventory:
	    print '''you now have item 1'''
	    inventory.append(prompt) 
	else:
	    print '''no item here'''
	    prompt_bedroom_room()	
    elif prompt == "2":
        print ''' Item 2 specifics '''
    elif prompt == "3":
        print ''' Item 3 specifics '''
    else:
	prompt_bedroom_room()

def library_room():
    global inventory
    print ''' Description/instructions'''
    prompt_library_room()

def prompt_library_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
        enter_castle()
    elif prompt == "1":
        print ''' Item 1 specifics '''
	if prompt not in inventory:
	    print '''you now have item 1'''
	    inventory.append(prompt) 
	else:
	    print '''no item here'''
	    prompt_library_room()	
    elif prompt == "2":
        print ''' Item 2 specifics '''
    elif prompt == "3":
        print ''' Item 3 specifics '''
    else:
	prompt_library_room()

start()
