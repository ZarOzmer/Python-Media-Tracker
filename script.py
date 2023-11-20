import os.path
import random

if not os.path.isfile('mediaTracker.csv'):
    with open('mediaTracker.csv', 'x') as mediaTracker:
        pass

def addMedia():
    mtype = input("What type of media is it? Ex: Game, TV Show, Webfiction")
    mname = input("What is the name of the peaice of media? Ex: Game Of Thrones")
    mfind = input("Where can you find the media? Ex: a URL, Your Steam Library, really whatever will help you find it later")
    with open("mediaTracker.csv", 'a') as mediaTracker:
        mediaTracker.write("{}|{}|{}\n".format(mtype, mname, mfind))






print(
'''Welcome to the Python Media Tracker. 
This aplication is intented to allow you to track pices of midea you'd like to consume and help alleviate ADHD bordem paralysis
\n \n'''
)
userIn = input(
"""What would you like to do today?  
If you would like at add a new piece of midea, type: -A 
If you have finnished a pice of media or no longer whant to consume it, type: -R
If you're board and want to consume some media, type: -B"""
)

