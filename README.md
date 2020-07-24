# Airport Metar Report Parser

A METAR report is a loose international semi-standard used by airports for reporting information about wind speeds, humidity, and weather conditions. This program parses a subset of these reports from a stream and keeps some running aggregates.

## Installation
- Make sure to have python3.X installed
```
https://www.python.org/downloads/
```
- Clone or download the repository locally
- Go into the terminal and in the main project directory, enter
```
chmod +x run_report.py
```
- To start the parser enter
```
./run_report.py
```

## Notes
- In the script, the user has a choice to manually enter their Metar report or generate a few hundred thousand reports
- When manually entering reports, the program checks for the validity of the reports
- The program generates only valid reports

## Metar Format
The report format looks like this:
```
<ICAO Code> <Timestamp> <Wind Info>
```
Which breaks down into this:

### ICAO Code
This is a string in the ASCII range of upper-case letters. It is at least one such character. It is terminated by a space after the final character.

Examples:

- YYZ
- A
- LAX
- BIRK

We’re not concerned about verifying the validity of these codes in this exercise. Parsing them is enough.

### Timestamp
This is a string in the format of:

```
<day of month><hours><minutes>Z
```

Where:

- day of month: 2 digits, the parsed number is in the range of 1-31 inclusive
- hours: 2 digits, the parsed number is in the range of 0-23 inclusive
- minutes: 2 digits, the parsed number in the range of 0-59

### Wind Info
This one is a little tricky. The METAR format specifies wind speeds in two different units: knots or meters per second. To complicate matters there is an optional gusts value.
```
<direction><speed><gusts?><unit>
```
Eg:
```
18027KT
180120MPS
01323G30MPS
```

The components of the format can be parsed as follows:

- direction: 3 digits
- speed: 2-3 digits, minimum 00
- gusts?: 2 digits, optional. When it appears, parsed as G23
- unit: Either KT or MPS
## Example Reports
```
YYZ 122201Z 12023MPS
LAX 022355Z 09332G78KT
FR 110232Z 001100G12MPS
```