#!/usr/bin/env python3
#
# This piece of code is licensed under CC BY 4.0 by deepstruck.
# Date: 2019-08-01
# Description: A simple interactive story written in Python3
# You can run this application on linux using 
# $ ./takeout.py
#	or
# $ python takeout.py

import random
import time

def displayIntro():
    print("It is towards the end of a long year.")
    print("")
    time.sleep(3)
    print("You have a craving for some chinese food and decide to leave")
    print("")
    time.sleep(3)
    print("Wow, it's really dark out")
    time.sleep(2)
    print ("")

def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Were you going to get the number one or the number two? (1 or 2): ")
    
    return path

def checkPath(chosenPath):
    print("You leave, contemplating how fresh the food will be on your plate")
    time.sleep(3)
    print ("")
    print("Amazing...You can't see anything at all!")
    time.sleep(3)
    print("A lamp flickers on as you pass underneath")
    print()
    time.sleep(3)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("You have arrived at the Chinese restaurant!")
        print("Mmmmmm! Tasty!")
        time.sleep(3)
    else:
        print("It's dark again...")
        time.sleep(3)
        print ("")
        time.sleep(2)
        print("You are hit by a vehicle!")
        time.sleep(1)
        print ("You are dead!")
        time.sleep(6)
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Would you like to try again? (yes or y to continue playing): ")
