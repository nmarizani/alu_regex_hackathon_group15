#:/usr/bin/python3
import re

pattern = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
text = "192.168.0.1"
input_string = input("Enter ip address: ")
matches = pattern.match(input_string)

if matches:
    print("Match found", input_string)
else:
    print("No match found")