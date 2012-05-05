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


class Room:
    
    
    def __init__(self, name):
	self.name = name
    

    def enter(self):
	print self.description
	self.prompt()

    def prompt(self):
	print "Pick an object"
	choice = raw_input('==> ')
	if(choice in self.options):
	    print "That worked"
	else:
	    print "didnt work"


try:
    open("rooms")
    stdin = file("rooms")
except:
    stderr.write("Error opening rooms\n")
    exit(1)

rooms = []
ind = 0
for line in stdin:
    rooms.append(Room(line))


rooms[0].options = ['Hand', 'Cage', 'Crevice']
rooms[0].description = "You are in the Dungeon"
rooms[1].description = "You are in the Kitchen"
rooms[0].enter()
