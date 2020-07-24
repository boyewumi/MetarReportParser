#!/usr/bin/python3

def is_valid_speed(wind_info):
    unit_idx = 0

    if "KT" not in wind_info and "MPS" not in wind_info:
        print("Speed unit needs to be in KT or MPS")
        return False
    else:
        if "KT" in wind_info:
            unit_idx = wind_info.index("KT")
        else:
            unit_idx = wind_info.index("MPS")
    if "G" in wind_info:
        gusts_idx = wind_info.index("G")
        if len(wind_info[3:gusts_idx]) < 2 or len(wind_info[3:gusts_idx]) > 3 or wind_info[3:gusts_idx].isdigit() == False:
            print("Speed needs to be 2-3 digts long")
            return False
        if len(wind_info[gusts_idx:unit_idx]) != 3:
            print("Gusts needs to start with the letter G and followed by 2 digits")
            return False
    else:
        if len(wind_info[3:unit_idx]) < 2 or len(wind_info[3:unit_idx]) > 3:
            print("Speed needs to be 2-3 digts long")
            return False
    return True

def is_valid_direction(wind_info):
    if wind_info[0:3].isdigit() == False:
        print("Direction needs to be 3 digits")
        return False
    return True
    
def is_valid_wind_info_len(wind_info):
    if len(wind_info) < 7:
        print("Wind information needs to be 7 characters or more")
        return False
    return True
    
def is_valid_time_stamp(time_stamp):
    if time_stamp[0:6].isdigit() == False or time_stamp[6] != "Z":
        print("Timestamp needs to be 6 digits and end with Z")
        return False
    return True

def is_valid_time_stamp_len(time_stamp):
    if len(time_stamp) != 7:
        print("Timestamp string needs to have a length of 7 characters")
        return False
    return True

def is_all_upper_case_letters(letter):
    if letter.isupper() == False:
        print("ICAO Code needs to be all upper case letters")
        return False
    return True

def is_valid_tokens_len(tokens):
    #we need 3 substrings for it to be a valid report
    if len(tokens) != 3:
        print("Report string needs to be 3 space seperated substrings ")
        return False
    return True

def tokenize_report(report):
    return report.split()

def is_valid_report(report):

    tokens = tokenize_report(report)
    if is_valid_tokens_len(tokens) == False:
        return False

    icao_code = str(tokens[0])
    time_stamp = str(tokens[1])
    wind_info = str(tokens[2])

    #check for validity of the report by analyzing the substrings from left to right
    if is_all_upper_case_letters(icao_code) == False:
        return False
    if is_valid_time_stamp_len(time_stamp) == False:
        return False
    if is_valid_time_stamp(time_stamp) == False:
        return False
    if is_valid_wind_info_len(wind_info) == False:
        return False
    if is_valid_direction(wind_info) == False:
        return False
    if is_valid_speed(wind_info) == False:
        return False

    return True