#!/usr/bin/python3

import collections
from MetarReportParser import reportGenerator
from MetarReportParser import reportParser
from MetarReportParser import validReportChecker

print("Welcome to the Metar Report Parser!")
userChoice = ""
#initializing nest dictionary
reportTallyDict = collections.defaultdict(dict)

while userChoice != "1" and userChoice != "2":

    userChoice = input("Enter 1 to manually enter reports. Enter 2 to generate a few hundred thousound reports\n")

    if userChoice == "1":
        report = ""

        while report != "quit":
            report = input("Please enter your a valid report or type 'quit' to exit\n")
            if report != "quit":
                if validReportChecker.isValidReport(report) == False:
                    print("Invalid report format, please try again")
                else:
                    reportParser.tallyReports(report, reportTallyDict)
            else:
                reportParser.summarizeReports(reportTallyDict)
                break
    elif userChoice == "2":
        for i in range(100000):

            generatedReport = reportGenerator.getGeneratedReport()
            reportTallyDict = reportParser.tallyReports(generatedReport, reportTallyDict)

        reportParser.summarizeReports(reportTallyDict)
        
        break
