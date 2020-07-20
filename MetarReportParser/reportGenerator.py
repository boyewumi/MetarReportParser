#!/usr/bin/python3

import random
from string import ascii_uppercase


def generateICAOCode():
    #generates random uppercase letters varying from length 3-4
    return ''.join(random.choice(ascii_uppercase) for i in range(3))

def generateDayOfMonth():
    dayOfMonth = random.randint(1, 31)
    #if we find that we have a number like 9, make it 09 to match our format better
    if len(str(dayOfMonth)) < 2:
        return "0" + str(dayOfMonth)
    else:
        return str(dayOfMonth)

def generateHour():
    #valid hour of the day is from 00 to 23
    hour = random.randint(0, 23)
    if len(str(hour)) < 2:
        return "0" + str(hour)
    else:
        return str(hour)

def generateMinute():
    minute = random.randint(0, 59)
    if len(str(minute)) < 2:
        return "0" + str(minute)
    else:
        return str(minute)

def generateDirection():
    #choose a random 3 digit integer from 100 to 999
    direction = random.randint(100, 999)
    return str(direction)

def generateSpeed():
    minute = random.randint(0, 999)
    if len(str(minute)) < 2:
        return "0" + str(minute)
    else:
        return str(minute)

def generateGusts():
    gusts = random.randint(10, 99)
    #gusts wind is recognizable with a G in from of the number. Also here we randomize the chances of having gust wind or not
    gustsOrNothing = ["G" + str(gusts), ""]
    return random.choice(gustsOrNothing)

def generateUnit():
    unit = ["KT", "MPS"]
    #randomize the choosing of unit
    return random.choice(unit)

def getGeneratedReport():
    #asseblem all value generators to make a random valid report
    return (generateICAOCode() + " " + generateDayOfMonth() + generateHour() + 
                    generateMinute() + "Z " + generateDirection() + generateSpeed() + generateGusts() + generateUnit())