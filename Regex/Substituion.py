#!/usr/bin/python3
import re

#basic subsistution
print()
print('Below is basic subsitution:')
nameRegex = re.compile(r'employee \w+')
print(nameRegex.sub('redacted', 'This is a test for employee john. employee john is testing.'))


#subsistution based on position ||||||| * or +
print()
print('Below is subsitution based on position (* -or- +):')
nameRegex = re.compile(r'employee (\w)\w*')
print(nameRegex.sub(r'\1****', 'This is a test for employee john. employee john is testing.'))
#can there be more than 1 group specified ...?


#manage complex regex w/ re.verbose
#example below - instead of:
#phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4} (\s*(ext|x|ext.)\s*\d{2,5})?)')
#use: 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
#someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)








