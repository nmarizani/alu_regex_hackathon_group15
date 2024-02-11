import re

pattern = re.compile('^(.+)\sS(\d{2})E(\d{2}): (.+)$')

title = "Friends S02E03: The One Where Heckles Dies"
input_string = input("Enter a tv episode title: ")
matches = pattern.match(input_string)

if matches:
    print("The title matches the pattern.")
else:
    print("The title does not match the pattern.")
