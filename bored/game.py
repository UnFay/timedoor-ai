# import modules
import time

#classes
# class Item:
#     def __init__(self, id, name, desc):
#         self.desc = desc

class Flag:
    def __init__(self, id, state):
        self.id = id,
        self.state = state

class Room:
    def __init__(self, id, name, roomDesc, currentFeatures=[]):
        self.id = id,
        self.name = name,
        self.roomDesc = roomDesc,
        self.currentFeatures = currentFeatures

class Feature:
    def __init__(self, id, desc, interactable = False, interact = None):
        self.id = id,
        self.desc = desc,
        self.interactable = interactable,
        self.interact = interact

#global constants & variables
delayPerCharacter = 0.08

inventory =[]
flags = []
currentRoom = "Room0"

rooms = [
    Room("Room0", "Room 0", 
         "Where you first found yourself. A mostly empty, plain room with white walls and a gray, carpeted floors.",
         currentFeatures=["Greg is just standing there."])
]

#functions
def monologue(character, lineArray, delayByLength = True, defaultDelay = 0, endDelay = 0):
    for line in lineArray: 
        print(character + ": " + line)
        if delayByLength: time.sleep(len(line)*delayPerCharacter)
        time.sleep(defaultDelay)
    time.sleep(endDelay)

def playerInput(options):
    i = 1
    print()
    for line in options:
        print("    ["+ str(i) + "]    " + line)
        i += 1
    print()
    while True:
        playerInput = input()
        if (playerInput.isdigit()):
            if(int(playerInput)>0 & int(playerInput)<=len(options)):
                return int(playerInput)
            else:
                print("Number is not one of the options!")
        else:
            print("Enter a number corresponding to an option!")
    
def lookAround():
    

#main
monologue("Guy", ["Hello world", "How are you today"])
playerInput(["I'm good, what about you", "*silence*", "(beat Guy up)"])