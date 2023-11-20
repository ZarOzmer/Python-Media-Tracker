import os.path
import random
import csv
import os

if not os.path.isfile('mediaTracker.csv'):
    with open('mediaTracker.csv', 'w') as mediaTracker:
        mediaTracker.write("Type|Name|Location\n")
        
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def addMedia():
    mtype = input("What type of media is it? Ex: Game, TV Show, Webfiction \n").capitalize()
    mname = input("What is the name of the peaice of media? Ex: Game Of Thrones \n")
    mfind = input("Where can you find the media? Ex: a URL, Your Steam Library, really whatever will help you find it later \n")
    with open("mediaTracker.csv", 'a') as mediaTracker:
        mediaTracker.write("{}|{}|{}\n".format(mtype, mname, mfind))

def getMeda():
    with open('MediaTracker.csv', newline='') as file:
        mediaCSV = csv.reader(file, delimiter = "|")
        next(mediaCSV)
        mediaList = []
        stype = input("what type of media do you want to consume? for any just hit enter \n").capitalize()
        
        for row in mediaCSV:
            if stype in row[0]:
                mediaList.append(row)
    if len(mediaList) > 1:
        media = mediaList[random.randint(0, (len(mediaList)) -1 )]
    elif len(mediaList) == 1: media = mediaList[0]
    else:
        print("You Have no media of that type saved")
        return()
    print("your media is: {name}, it is a {type} that can be found at {location}.\n".format(name = media[1], type = media[0], location = media[2]))

    




while True:
    clear()
    print(
    '''Welcome to the Python Media Tracker. 
    This aplication is intented to allow you to track pices of midea you'd like to consume and help alleviate ADHD bordem paralysis
    '''
    )
    userIn = input(
    """What would you like to do today?  
    If you would like at add a new piece of midea, type: -A 
    If you have finnished a pice of media or no longer whant to consume it, type: -R
    If you're board and want to consume some media, type: -B
    if you're done with the program type: -E
    """
    )
    if userIn == '-A':
        addMedia()
    elif userIn == '-B':
        getMeda()
    elif userIn == '-E':
        break
    temp =input("press enter when you're done with what's currently on screen")