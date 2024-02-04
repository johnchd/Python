#/usr/bin/python3

import re

print(' ---- PART 1 ----')
#search - display 1st object found
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242. test 440-5940-3303')
print('Method 1: ' + mo.group())


#findall - display all objects found
print()
print('Method 2:')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print( phoneNumRegex.findall('My number is 415-555-4242 this is a test 233-403-3043'))

#findall - display all objects found
print()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.findall('My number is 415-555-4242 test 440-303-3049')
print('Method 3: ' + str(mo1))

#findall - display all objects found
print()
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo1 = phoneNumRegex.findall('My number is 415-555-4242 test 440-303-3049')
print('Method 4: {} ' + str(mo1))

#############
####################################################
#############
#############
#############
#############

#grouping w/ parentheses
print('\n---- PART 2 ---- Group w/ parentheses')

#print group 1, 2, 3
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.search('My number is 415-555-4242')
print('group 2: ' + str(mo1.group(2)))

#print ALL groups (notice mo1.group(S))
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.search('My number is 415-555-4242 test 440-304-3403')
print('All groups: ' + str(mo1.groups()))

#assing variables to groups
print()
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex.search('My number is 415-555-4242 test.')
areaCode, mainNumber = mo1.groups()
print('area code: ' + str(areaCode))
print('main number: ' + str(mainNumber))
#line 54 is dependent on the amount of groups in line 52. 

