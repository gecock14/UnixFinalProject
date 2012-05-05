#!/usr/bin/env python

#Imports and setup
import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

#Global variables
global keys
keys = 0
global defeated
defeated = []
global inventory
inventory = []


class searchRoom:
    
    
    def __init__(self, name):
	self.name = name
    

    def enter(self):
	print self.description
	print "Rooms:"
	for option in self.destinations:
	    print option,
	self.prompt()


    def prompt(self):
	print "\nPick a room: "
	self.checkForKey()
	choice = raw_input('==> ')
	if(choice in self.destinations and choice != 'Boss'):
	    self.gotoRoom(self.destinations[choice])
	elif(choice == 'Boss' and keys != 2):
	    print "You need two keys to get in"
	    self.gotoRoom(4)
	elif(choice == 'Boss' and keys == 2):
	    print "You face the Boss!"
	    endGame()
	else:
	    print "didnt work"

    def gotoRoom(self, where):
	rooms[where].enter()

    def checkForKey(self):
	global keys
	keys = keys + self.key
	print "Keys: ", keys

def endGame():
    exit(0)

try:
    open("rooms")
    stdin = file("rooms")
except:
    stderr.write("Error opening rooms\n")
    exit(1)

global keys
keys = 0
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
rooms[4].destinations = {'Dungeon':0, 'Kitchen':1, 'Bedroom':2, 'Library':3, 'Boss':5}
rooms[4].description = "You are in the Hallway"
rooms[5].key = 0
rooms[5].destinations = {'Hallway':4}
rooms[5].description = "You are in the Boss room"


rooms[4].enter()
