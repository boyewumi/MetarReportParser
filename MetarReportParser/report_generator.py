#!/usr/bin/python3

import random
from string import ascii_uppercase


def generate_icao_code():
    #generates random uppercase letters varying from length 3
    return ''.join(random.choice(ascii_uppercase) for i in range(3))

def generate_day_of_month():
    day_of_month = random.randint(1, 31)
    #if we find that we have a number like 9, make it 09 to match our format better
    if len(str(day_of_month)) < 2:
        return "0" + str(day_of_month)
    else:
        return str(day_of_month)

def generate_hour():
    #valid hour of the day is from 00 to 23
    hour = random.randint(0, 23)
    if len(str(hour)) < 2:
        return "0" + str(hour)
    else:
        return str(hour)

def generate_minute():
    minute = random.randint(0, 59)
    if len(str(minute)) < 2:
        return "0" + str(minute)
    else:
        return str(minute)

def generate_direction():
    #choose a random 3 digit integer from 100 to 999
    direction = random.randint(100, 999)
    return str(direction)

def generate_speed():
    minute = random.randint(0, 999)
    if len(str(minute)) < 2:
        return "0" + str(minute)
    else:
        return str(minute)

def generate_gusts():
    gusts = random.randint(10, 99)
    #gusts wind is recognizable with a G in from of the number. Also here we randomize the chances of having gust wind or not
    gusts_or_nothing = ["G" + str(gusts), ""]
    return random.choice(gusts_or_nothing)

def generate_unit():
    unit = ["KT", "MPS"]
    #randomize the choosing of unit
    return random.choice(unit)

def get_generated_report():
    #assemble all value generators to make a random valid report
    return (generate_icao_code() + " " + generate_day_of_month() + generate_hour() + 
            generate_minute() + "Z " + generate_direction() + generate_speed() + generate_gusts() + generate_unit())