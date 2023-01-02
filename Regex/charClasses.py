#!/usr/bin/python3

import re

print()
print('Find pattern out of text:')
test = re.compile(r'\d+\s\w+')
x = test.findall('''12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge''')
print(x)

#Create own character class
print()
print('Find all vowels (upper/lower case)')
myOwn = re.compile(r'[aeiouAEIOU]')
x = myOwn.findall('Hello this is a test for Python Regex.')
print(x)

print()
print('Find all BUT vowels (upper/lower case) ---- use the^ ')
myOwn = re.compile(r'[^aeiouAEIOU]')
x = myOwn.findall('Hello this is a test for Python Regex.')
print(x)