#!/usr/bin/python3

def getWindInfoValues(windInfo):
    windInfoDict = {
        "direction" : 0,
        "speed" : 0,
        "gusts" : 0
    }

    #get the first 3 digits of the string as the direction
    windInfoDict["direction"] = int(windInfo[:3])

    if "KT" in windInfo:
        unitIdx = windInfo.index("KT")
    else:
        unitIdx = windInfo.index("MPS")


    if "G" in windInfo:
        gustsIdx = windInfo.index("G")
        #we know that speed is after direction and before gusts if it exists
        windInfoDict["speed"] = int(windInfo[3:gustsIdx])
        #gustsIdx + 1 to skip the G
        windInfoDict["gusts"] = int(windInfo[gustsIdx+1:unitIdx])
        if "KT" in windInfo:
            #normalize knots to meters per second
            windInfoDict["speed"] = windInfoDict["speed"] // 2
            windInfoDict["gusts"] = windInfoDict["gusts"] // 2
    else:
        windInfoDict["speed"] = int(windInfo[3:unitIdx])
        if "KT" in windInfo:
            windInfoDict["speed"] = windInfoDict["speed"] // 2

    return windInfoDict

def getTimeStampValues(timeStamp):
    timeStampDict = {
        "dayOfMonth" : 0,
        "hours" : 0,
        "minutes" : 0
    }

    #we know each value is going to be 2 digits each
    timeStampDict["dayOfMonth"] = int(timeStamp[:2])
    timeStampDict["hours"] = int(timeStamp[2:4])
    timeStampDict["minutes"] = int(timeStamp[4:6])

    return timeStampDict
    
def tokenizeReport(report):
    return report.split()

def getReportInfo(report):
    reportDict = {
        "icaoCode" : "",
        "dayOfMonth" : 0,
        "hours" : 0,
        "minutes" : 0,
        "direction" : 0,
        "speed" : 0,
        "gusts" : 0
    }

    tokens = tokenizeReport(report)
    #add parsed information into the report dictionary
    reportDict["icaoCode"] = tokens[0]
    reportDict.update(getTimeStampValues(tokens[1]))
    reportDict.update(getWindInfoValues(tokens[2]))

    return reportDict

def tallyReports(report, reportTallyDict):
    reportDict = getReportInfo(report)

    #if the icao code already exists as the key for our nested dictionary then update the information or else make a new nested key value pair
    if reportDict["icaoCode"] in reportTallyDict.keys():
        #update merges two dictionaries without overwriting the other pairs that are not included like the report's total speed
        reportTallyDict[reportDict["icaoCode"]].update(reportDict)
        reportTallyDict[reportDict["icaoCode"]]["numTimesReported"] += 1
        reportTallyDict[reportDict["icaoCode"]]["totalSpeed"] += reportTallyDict[reportDict["icaoCode"]]["speed"]
        reportTallyDict[reportDict["icaoCode"]]["avgWindSpeedPerAirport"] = reportTallyDict[reportDict["icaoCode"]]["totalSpeed"] // reportTallyDict[reportDict["icaoCode"]]["numTimesReported"]
    else:
        reportTallyDict[reportDict["icaoCode"]] = {}
        reportTallyDict[reportDict["icaoCode"]] = reportDict
        reportTallyDict[reportDict["icaoCode"]]["numTimesReported"] = 1
        reportTallyDict[reportDict["icaoCode"]]["totalSpeed"] = reportTallyDict[reportDict["icaoCode"]]["speed"]
        reportTallyDict[reportDict["icaoCode"]]["avgWindSpeedPerAirport"] = reportTallyDict[reportDict["icaoCode"]]["speed"]
    
    return reportTallyDict

def summarizeReports(reportTallyDict):
    #final report after reading stream based on our nested dictionary
    for key in reportTallyDict:
        print("The current windspeed for ICAO Code", key + " is: " + str(reportTallyDict[key]["speed"]) + "MPS with the gusts of " + 
            str(reportTallyDict[key]["gusts"]) + "MPS during day " + str(reportTallyDict[key]["dayOfMonth"]) + 
            " at time " + str(reportTallyDict[key]["hours"]) + ":" + str(reportTallyDict[key]["minutes"]) + ". " + key +" also has an average of " + 
            str(reportTallyDict[key]["avgWindSpeedPerAirport"]) + "MPS out of " + str(reportTallyDict[key]["numTimesReported"]) + " reports")
