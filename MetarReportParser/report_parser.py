#!/usr/bin/python3

def get_wind_info_values(wind_info):
    wind_info_dict = {
        "direction" : 0,
        "speed" : 0,
        "gusts" : 0
    }

    #get the first 3 digits of the string as the direction
    wind_info_dict["direction"] = int(wind_info[:3])

    if "KT" in wind_info:
        unit_idx = wind_info.index("KT")
    else:
        unit_idx = wind_info.index("MPS")


    if "G" in wind_info:
        gusts_idx = wind_info.index("G")
        #we know that speed is after direction and before gusts if it exists
        wind_info_dict["speed"] = int(wind_info[3:gusts_idx])
        #gusts_idx + 1 to skip the G
        wind_info_dict["gusts"] = int(wind_info[gusts_idx+1:unit_idx])
        if "KT" in wind_info:
            #normalize knots to meters per second
            wind_info_dict["speed"] = wind_info_dict["speed"] // 2
            wind_info_dict["gusts"] = wind_info_dict["gusts"] // 2
    else:
        wind_info_dict["speed"] = int(wind_info[3:unit_idx])
        if "KT" in wind_info:
            wind_info_dict["speed"] = wind_info_dict["speed"] // 2

    return wind_info_dict

def get_timestamp_values(time_stamp):
    time_stamp_dict = {
        "dayOfMonth" : 0,
        "hours" : 0,
        "minutes" : 0
    }

    #we know each value is going to be 2 digits each
    time_stamp_dict["dayOfMonth"] = int(time_stamp[:2])
    time_stamp_dict["hours"] = int(time_stamp[2:4])
    time_stamp_dict["minutes"] = int(time_stamp[4:6])

    return time_stamp_dict
    
def tokenize_report(report):
    return report.split()

def get_report_info(report):
    report_dict = {
        "icaoCode" : "",
        "dayOfMonth" : 0,
        "hours" : 0,
        "minutes" : 0,
        "direction" : 0,
        "speed" : 0,
        "gusts" : 0
    }

    tokens = tokenize_report(report)
    #add parsed information into the report dictionary
    report_dict["icaoCode"] = tokens[0]
    report_dict.update(get_timestamp_values(tokens[1]))
    report_dict.update(get_wind_info_values(tokens[2]))

    return report_dict

def tally_reports(report, report_tally):
    report_dict = get_report_info(report)

    #if the icao code already exists as the key for our nested dictionary then update the information or else make a new nested key value pair
    if report_dict["icaoCode"] in report_tally.keys():
        #update merges two dictionaries without overwriting the other pairs that are not included like the report's total speed
        report_tally[report_dict["icaoCode"]].update(report_dict)
        report_tally[report_dict["icaoCode"]]["numTimesReported"] += 1
        report_tally[report_dict["icaoCode"]]["totalSpeed"] += report_tally[report_dict["icaoCode"]]["speed"]
        report_tally[report_dict["icaoCode"]]["avgWindSpeedPerAirport"] = report_tally[report_dict["icaoCode"]]["totalSpeed"] // report_tally[report_dict["icaoCode"]]["numTimesReported"]
    else:
        report_tally[report_dict["icaoCode"]] = {}
        report_tally[report_dict["icaoCode"]] = report_dict
        report_tally[report_dict["icaoCode"]]["numTimesReported"] = 1
        report_tally[report_dict["icaoCode"]]["totalSpeed"] = report_tally[report_dict["icaoCode"]]["speed"]
        report_tally[report_dict["icaoCode"]]["avgWindSpeedPerAirport"] = report_tally[report_dict["icaoCode"]]["speed"]
    
    return report_tally

def summarize_reports(report_tally):
    #final report after reading stream based on our nested dictionary
    for key in report_tally:
        print("The current windspeed for ICAO Code", key + " is: " + str(report_tally[key]["speed"]) + "MPS with the gusts of " + 
            str(report_tally[key]["gusts"]) + "MPS during day " + str(report_tally[key]["dayOfMonth"]) + 
            " at time " + str(report_tally[key]["hours"]) + ":" + str(report_tally[key]["minutes"]) + ". " + key +" also has an average of " + 
            str(report_tally[key]["avgWindSpeedPerAirport"]) + "MPS out of " + str(report_tally[key]["numTimesReported"]) + " reports")
