import random
import csv
import os

if not os.path.isfile('mediaTracker.csv'):
    with open('mediaTracker.csv', 'w') as mediaTracker:
        mediaTracker.write("Type|Name|Location\n")
        
def clear():
    #for windowsOS
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

def getMedia():
    with open('MediaTracker.csv', newline='') as file:
        mediaCSV = csv.reader(file, delimiter = "|")
        next(mediaCSV)
        mediaList = []
        stype = input("what type of media do you want to consume? for any just hit enter \n").capitalize()
    #creates a list of all the media of a certen type or if no type given a list of all the media the program tracks
        for row in mediaCSV:
            if stype in row[0]:
                mediaList.append(row)
    #selects a random peice of media from that list
    if len(mediaList) > 1:
        media = mediaList[random.randint(0, (len(mediaList)) -1 )]
    #unless the list is to short
    elif len(mediaList) == 1: media = mediaList[0]
    else:
        print("You Have no media of that type saved")
        return()
    print("your media is: {name}, it is a {type} that can be found at {location}.\n".format(name = media[1], type = media[0], location = media[2]))

def removeMedia():
    mtype = str(input("What kind of media are you removing?\n").capitalize())
    medialist = []
    with open('MediaTracker.csv', newline='') as file:
        mediaCSV = csv.reader(file, delimiter = "|")
        next(mediaCSV)
    #generates a list of all the media of the given type
        for row in mediaCSV:
                print(row[0])
                print(mtype)
                print(mtype in row[0])
                print("")
                if mtype in row[0]:
                    medialist.append(row)
    #prunes the list of media who's names dont contane a search string
    mserch = input("search criteria for the name of the media you wish to remove\n")
    for row in medialist:
        if not mserch.lower() in str(row[1]).lower():
            medialist.remove(row)
    if not len(medialist) > 0:
        print("No media matches your serch criteria")
        return
    for x in range(len(medialist)):
        print(str(x) + ": " + str(medialist[x]))
    input3 = input("enter the number of the media you wish to remove\n")
    #what's to be removed 
    badMedia = medialist[int(input3)]
    #generates a list of everthing not removed
    goodMedia = []
    with open('MediaTracker.csv', ) as file:
        mediaCSV = csv.reader(file, delimiter = "|")
        next(mediaCSV)
        for row in mediaCSV:
            if not row == badMedia:
                goodMedia.append(row)
    #overwrites the file with the list of not removed things after adding the header
    with open('MediaTracker.csv', 'w') as mediaCSV:
        mediaCSV.write("Type|Name|Location\n")
        for line in goodMedia:
            mediaCSV.write("{}|{}|{}\n".format(line[0],line[1],line[2]))





while True:
    clear()
    print(
    '''Welcome to the Python Media Tracker. 
    This aplication is intented to allow you to track pieces of midea you'd like to consume and help alleviate ADHD boredom paralysis
    '''
    )
    userIn = input(
    """What would you like to do today?  
    If you would like at add a new piece of midea, type: -A 
    If you have finnished a piece of media or no longer whant to consume it, type: -R
    If you're board and want to consume some media, type: -B
    if you're done with the program type: -E
    """
    )
    if userIn == '-A':
        addMedia()
    elif userIn == '-B':
        getMedia()
    elif userIn == '-E':
        exit()
    elif userIn == '-R':
        removeMedia()
    temp =input("press enter when you're done with what's currently on screen")

