#!/usr/bin/python3

def isValidSpeed(windInfo):
    unitIdx = 0

    if "KT" not in windInfo and "MPS" not in windInfo:
        print("Speed unit needs to be in KT or MPS")
        return False
    else:
        if "KT" in windInfo:
            unitIdx = windInfo.index("KT")
        else:
            unitIdx = windInfo.index("MPS")
    if "G" in windInfo:
        gustsIdx = windInfo.index("G")
        if len(windInfo[3:gustsIdx]) < 2 or len(windInfo[3:gustsIdx]) > 3 or windInfo[3:gustsIdx].isdigit() == False:
            print("Speed needs to be 2-3 digts long")
            return False
        if len(windInfo[gustsIdx:unitIdx]) != 3:
            print("Gusts needs to start with the letter G and followed by 2 digits")
            return False
    else:
        if len(windInfo[3:unitIdx]) < 2 or len(windInfo[3:unitIdx]) > 3:
            print("Speed needs to be 2-3 digts long")
            return False
    return True

def isValidDirection(windInfo):
    if windInfo[0:3].isdigit() == False:
        print("Direction needs to be 3 digits")
        return False
    return True
    
def isValidWindInfoLen(windInfo):
    if len(windInfo) < 7:
        print("Wind information needs to be 7 characters or more")
        return False
    return True
    
def isValidTimeStamp(timestamp):
    if timestamp[0:6].isdigit() == False or timestamp[6] != "Z":
        print("Timestamp needs to be 6 digits and end with Z")
        return False
    return True

def isValidTimeStampLen(timestamp):
    if len(timestamp) != 7:
        print("Timestamp string needs to have a length of 7 characters")
        return False
    return True

def isAllUpperCaseLetters(letter):
    if letter.isupper() == False:
        print("ICAO Code needs to be all upper case letters")
        return False
    return True

def isValidTokensLen(tokens):
    #we need 3 substrings for it to be a valid report
    if len(tokens) != 3:
        print("Report string needs to be 3 space seperated substrings ")
        return False
    return True

def tokenizeReport(report):
    return report.split()

def isValidReport(report):

    tokens = tokenizeReport(report)
    if isValidTokensLen(tokens) == False:
        return False

    icaoCode = str(tokens[0])
    timestamp = str(tokens[1])
    windInfo = str(tokens[2])

    #check for validity of the report by analyzing the substrings from left to right
    if isAllUpperCaseLetters(icaoCode) == False:
        return False
    if isValidTimeStampLen(timestamp) == False:
        return False
    if isValidTimeStamp(timestamp) == False:
        return False
    if isValidWindInfoLen(windInfo) == False:
        return False
    if isValidDirection(windInfo) == False:
        return False
    if isValidSpeed(windInfo) == False:
        return False

    return True