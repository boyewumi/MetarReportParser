#!/usr/bin/python3

import collections
from MetarReportParser import report_generator
from MetarReportParser import report_parser
from MetarReportParser import valid_report_checker

print("Welcome to the Metar Report Parser!")
user_choice = ""
#initializing nest dictionary
report_tally = collections.defaultdict(dict)

while user_choice != "1" and user_choice != "2":

    user_choice = input("Enter 1 to manually enter reports. Enter 2 to generate a few hundred thousound reports\n")

    if user_choice == "1":
        report = ""

        while report != "quit":
            report = input("Please enter your a valid report or type 'quit' to exit\n")
            if report != "quit":
                if valid_report_checker.is_valid_report(report) == False:
                    print("Invalid report format, please try again")
                else:
                    report_tally = report_parser.tally_reports(report, report_tally)
            else:
                report_parser.summarize_reports(report_tally)
                break
    elif user_choice == "2":
        for i in range(100000):

            generated_report = report_generator.get_generated_report()
            report_tally = report_parser.tally_reports(generated_report, report_tally)

        report_parser.summarize_reports(report_tally)
        
        break
