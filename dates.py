#!/usr/bin/python3

import re

date_regex = r'\d{2}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}'

# Example usage:
date_string = '01-Jan-2023'
if re.match(date_regex, date_string):
    print('Valid date')
else:
    print('Invalid date')
