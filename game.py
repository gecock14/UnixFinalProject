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
    print "Welcome to The Thing Behind the Walls!"
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
    print "The gentle pitter-platter of falling condensation hitting cold stone stirs you from your sleep. The room is"
    print "cold...much too cold in fact. A door slams and a blast of air rushes across your bare face and your eyes snap"
    print "open in horror. Who are you? Where are you? Your mind screams in the realization that you have no memory, no" 
    print "anything. You blink into the darkness trying to adjust to the minimal lighting, and slowly the outline of the"
    print "door that must have been shut appears. You struggle to your feet, every joint screaming in protest, and"
    print "trudge towards the door, your heart beat seeming louder with each step."
    print "Press 's' to start your adventure."
    while(1):
	choice = raw_input('==> ').lower()
	if choice == 'quit':
            exit(0)
    	elif choice == 's':
	    enter_castle()
    	else:
            print "That's not an option, try 's' to enter the castle or 'quit' to end the game.\n"


def enter_castle():
    global keys
    os.system('clear')
    print "You reach the door and push slowly, and with a loud creak, you find yourself looking down dank, dripping hallway. The smell of mold invades your nostrils,"
    print "souring your expression. You again wonder, where you are, or even who you are, terror rising in your throat."
    print "Summoning the stregth to carry on, you take small steps, investigating the 7 doors branching off the grim"
    print "grotto. The first door is labeled 'Dungeon', and you discover that it is from here the foul stench eminates."
    print "Next to it is a door labeled 'Bedroom', and you notice it is opened just a small crack. On the other side of"
    print "hall are two more doors, the first labeled 'Kitchen', and the other, 'Library'. Making your way past all these"
    print "doors, you see at the end of the hall, a set of three doors side by side. Just the sight of the 'middle' door"
    print "causes your stomach to roll over, and upon closer inspection, you notice that it has a set of two key holes"
    print "in it. A loud bang from other side startles you, but once you've calmed down you take a look at the two"
    print "flanking doors. The one to the 'left' seems to have scratch marks all over it, and the one to the 'right' seems"
    print "to have a dark liquid fluid out from underneath it. The choice is yours, which room do you enter?"

    if(inventory):
	print "Inventory: ", inventory
    print "Keys: ",keys
    while(1):
        choice = raw_input('==> ').lower()
        if (choice == 'quit'):
            exit(0)
        elif (choice == 'left'):
            werewolf_room()
        elif (choice == 'right'):
            vampire_room()
        elif(choice == 'middle' and keys is 2):
            bigboss_room()
	elif(choice == 'middle' and keys != 2):
	    print "You must obtain the two keys to open this door."
	    return_main()
	elif(choice == 'dungeon'):
	    dungeon_room()
	elif(choice == 'kitchen'):
	    kitchen_room()
	elif(choice == 'library'):
	    library_room()
	elif(choice == 'bedroom'):
	    bedroom_room()


def werewolf_room():
    global inventory
    print "With a touch of your hand, the claw-marked door gives way. Peering in you are startled by a blast of"
    print "warm air to the face. Suddenly aware that you are not alone, you flick a match, and find yourself face"
    print "face with a mangy coat of fur and a terrifying set of teeth. You're staring a werewolf in the face!"
    print" What do you do?!?"
    if('pistol with silver bullets' not in inventory):
	kicked("You have no way of fighting such a beast, what is it you need again? Silver bullets?")
    else:
	use_item("werewolf", "pistol with silver bullets")


def vampire_room():
    global inventory
    print "Fighting your revulsion at the sight of what is now clearly seeping blood, you push the door inwards"
    print "and view the room inside. You see what seems to be a coffin in the middle of the room, and approach it"
    print "peering inside. You reel back in disgust as you lay eyes on the bloated and disgusting figure laying"
    print "within. To your rising horror, the pale monstrosity sits up...and smiles at you. What do you do?!?"
    if('wooden stake' not in inventory):
        kicked("You have no way of stopping him, you stumble out of the room, slamming the door behind you, and holding back the rising bile in your throat.")
    else:
        use_item("vampire", "wooden stake")


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
    print "You blink, and blink again in the darkness. You realize that you're in your own bed, in your own house! It was"
    print "just a dream! Feeling infinitly better, you retreat back under your covers. In the gloom, you hear you closet door"
    print "creak open..."
    print "The End...?"
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
	print "The beast lunges at you, narrowly missing your outstretched arm. You whip your pistol around and put two rounds"
	print "between his eyes. Pulling the key off from around his neck, you continue onwards."
    elif(boss == "vampire"):
	print "Summoning you last vestigaes of courage, you jab the wooden stake into the vampires heart, and"
	print "The vampire burns away, revealing a key. You bend down and take the key."
    return_main()

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
    print "You open the door an a wall of stench hits you like a brick. Determined none-the-less, you begin"
    print "down a long set of stairs. Upon reaching the landing, you peer into the gloom, and are taken agasht"
    print "by what you see. This was clearly used as a torture chamber, filled from wall to wall with terrible"
    print "looking contraptions and sharp, terrifying instruments of indeterminate use. There seems to be three"
    print "places to of intrest; a decaying skeleton's 'hand', the back of a rusting torture 'cage', and a long"
    print "deep 'crevice' in the back wall. Where do you search?"
    prompt_dungeon_room()

def prompt_dungeon_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
	enter_castle()
    elif prompt == "hand":
        print "You discover a wooden stake grasped between the rotting finger, and carefully pry it out"
	if 'pistol with silver bullets' not in inventory:
	    print "You now have a wooden stake"
	    inventory.append('wooden stake')
	else:
	    print "You have already taken the item from there"	
    elif prompt == "cage":
	print "Investigation reveals a few scurrying rats, but nothing of value."
    elif prompt == "crevice":s
	print "You don't want to stick your hand in this dark crack, but you want to leave this castle even more. You gingerly"
	print "insert your finger and begin to search the cranies when you feel a light brush against the back of your hand.s"
	print "Yanking your hand out in a panic, dozens of spiders crawl away. Nothing in there." 
    prompt_dungeon_room()	


def kitchen_room():
    global inventory
    print "The door grates open with a terrible screech, exposing a kitchen in total disarray. Half decayed food"
    print "and other wet matter youd rather not guess about, coveres the floor with a sticky layer of film. "
    print "Silverware is strewn about, and all of the doors and drawers hang agape. Three places of intrest present"
    print "themselves; the knife 'drawer', the 'pantry', and the liquid-filled 'sink'. Where do you search?"
    prompt_kitchen_room()

def prompt_kitchen_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
        enter_castle()
    elif prompt == "drawer":
        print "You sneek a peek inside, and see a glitter of silver, and assume it to be silverware. A more through investigation"
	print "reveals a surprise: a pistol, equiped with what seems to be silver bullets." 
        if 'wooden stake' not in inventory:
            print "You now have a pistol with silver bullets"
	    inventory.append('pistol with silver bullets')
    	else:
	    print '''no item here'''
    elif prompt == "pantry":
        print "The collapsed store room reveals nothing but moldy food and scurrying insects. Nothing in here."
    elif prompt == "sink":
	print "Pluging your nose with one hand, you dunk the other into the filth and seach the basin via touch. Nothing in here."
    prompt_kitchen_room()



def bedroom_room():
    global inventory
    print "As the door creaks open, and you slink in as quietly as possible, it occurs to you that this room is"
    print "spotless and clean...until you glance at the sheets and see that they are covered in blood. Mildly"
    print "disturbed, you glance around, and see two more places of intrest; under the bed itself, and inside"
    print "an ornate and gothic dresser to the side. Where do you search, the 'sheets', the 'dresser', or 'under' the bed?"
    prompt_bedroom_room()

def prompt_bedroom_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
        enter_castle()
    elif prompt == "sheets":
        print "Pulling back the sheets, you find the source of the blood: a rat. There isn't much left however, "
	print "whatever did this is a force to be reckoned with."	
    elif prompt == "dresser":
        print "Pulling open the door, a black figure jumps out and at your face. Smacking with your hand, you notice that it"
	print "is a bat, and calm down as it flies away. Nothing else of value in here"
    elif prompt == "under":
        print "Gathering your courage, you lean over, and prepare to lift the skirt. You sneek a quick peek, and are relieved"
	print "that nothing is waiting for you. However, there is nothing of value."
    prompt_bedroom_room()

def library_room():
    global inventory
    print "The door to the library opens efortlessly, exposing the winding stairs within. Taking them upwards,"
    print "you enter into a study, lined with bookshelves and curios. Three items catch your eye, a conspicuous"
    print "'bookshelf', a 'desk', and a 'globe'. Which do you search?"
    prompt_library_room()

def prompt_library_room():
    global inventory
    prompt = raw_input('==> ').lower()
    if prompt == "b":
        enter_castle()
    elif prompt == "bookshelf":
        print "You peruse the shelf, seeing strange title like 'Necromicon' and 'Grimore Auditora', as well as dozens of"
	print "book titles that seem to be in another languge. Quite interesting, but not useful in the least."
    elif prompt == "desk":
        print "You find nothing but a few sheets of paper written in an oblique language."
    elif prompt == "globe":
        print "It's interesting because it doesn't seem to be a globe of Earth, but otherwise nothing useful."
    prompt_library_room()

start()
