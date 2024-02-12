#:/usr/bin/python3
import re

pattern = re.compile('#([0-9a-fA-F]{6})')
text = "#FF0000"
input_string = input("Enter a hex color: ")
matches = pattern.match(input_string)

if matches:
    print("Match found", input_string)
else:
    print("No match found")