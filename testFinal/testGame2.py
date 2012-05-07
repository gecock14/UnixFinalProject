#!/usr/bin/env python

#Imports and setup
import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

#Global variables
global keyint

global visited
visited = []
keyint = 0


class searchRoom:
    
    
    def __init__(self, name):
	self.name = name
    

    def enter(self):
	print "\n",self.description
	print "Rooms:",
	for option in self.destinations:
	    print option,
	print ""
	self.prompt()


    def prompt(self):
	self.checkForKey()
	print "Pick a room: "
	choice = raw_input('==> ')
	if(choice in self.destinations):
	    if(self.destinations[choice] == 5 and keyint != 2):
	    	print "\nYou need two keys to escape!"
	    	self.gotoRoom(4)
	    elif(self.destinations[choice] == 5 and keyint == 2):
	    	print "You've escaped!"
	    	endGame()
	    else:
		self.gotoRoom(self.destinations[choice])
	else:
	    print "\nInvalid Room"
	    self.enter()


    def gotoRoom(self, where):
	rooms[where].enter()


    def checkForKey(self):
	if(self.name not in visited):
	    global keyint
            if(self.key == "1\n"):
	        keyint = keyint + 1
	    visited.append(self.name)
	print "Keys: ", keyint
	


def endGame():
    exit(0)

try:
    open("rooms")
    stdin = file("rooms")
except:
    stderr.write("Error opening rooms\n")
    exit(1)

rooms = []


for line in stdin:
    rooms.append(searchRoom(line))

try:
    open("keys")
    stdin = file("keys")
except:
    stderr.write("Error opening keys\n")
    exit(1)

keys = []


for line in stdin:
    keys.append(line)

try:
    open("descriptions")
    stdin = file("descriptions")
except:
    stderr.write("Error opening descriptions\n")
    exit(1)

descriptions = []


for line in stdin:
    descriptions.append(line)

#try:
#    open("destinations")
#    stdin = file("destinations")
#except:
#    stderr.write("Error opening destinations\n")
#    exit(1)

#destinations = []


#for line in stdin:
#    destinations.append(line)

ind = 0
for ind in range(0, 6):
    rooms[ind].key = keys[ind]
    rooms[ind].description = descriptions[ind]

rooms[0].destinations = {'Hallway':4}
rooms[1].destinations = {'Hallway':4}
rooms[2].destinations = {'Hallway':4}
rooms[3].destinations = {'Hallway':4}
rooms[4].destinations = {'Dungeon':0, 'Kitchen':1, 'Bedroom':2, 'Library':3, 'Escape':5}
rooms[5].destinations = {'Hallway':4}



os.system('clear')
rooms[4].enter()
