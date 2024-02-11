#:/usr/bin/python3
import re

pattern = re.compile('^Why did the .*? ?Because.*$')
text = "Why did the cat jump on the table? Because it wanted to. Why did the chicken cross the road? Because it wanted to get to the other side."
input_string = input("Enter a joke: ")
matches = pattern.match(input_string)

if matches:
    print("Match found", input_string)
else:
    print("No match found")

