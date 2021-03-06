#!/usr/bin/env python

#Imports and setup
import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

#Global variables
global keys
keys = 0
global visited
visited = []


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
	    if(self.destinations[choice] == 5 and keys != 2):
	    	print "\nYou need two keys to escape!"
	    	self.gotoRoom(4)
	    elif(self.destinations[choice] == 5 and keys == 2):
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
	    global keys
	    keys = keys + self.key
	    visited.append(self.name)
	print "Keys: ", keys
	


def endGame():
    exit(0)

try:
    open("rooms")
    stdin = file("rooms")
except:
    stderr.write("Error opening rooms\n")
    exit(1)

rooms = []
ind = 0

for line in stdin:
    rooms.append(searchRoom(line))


rooms[0].key = 1
rooms[0].destinations = {'Hallway':4}
rooms[0].description = "You are in the Dungeon"
rooms[1].key = 1
rooms[1].destinations = {'Hallway':4}
rooms[1].description = "You are in the Kitchen"
rooms[2].key = 0
rooms[2].destinations = {'Hallway':4}
rooms[2].description = "You are in the Bedroom"
rooms[3].key = 0
rooms[3].destinations = {'Hallway':4}
rooms[3].description = "You are in the Library"
rooms[4].key = 0
rooms[4].destinations = {'Dungeon':0, 'Kitchen':1, 'Bedroom':2, 'Library':3, 'Escape':5}
rooms[4].description = "You are in the Hallway"
rooms[5].key = 0
rooms[5].destinations = {'Hallway':4}
rooms[5].description = "You've Escaped This Time"

os.system('clear')
rooms[4].enter()
