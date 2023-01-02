#!/usr/bin/python3
import re

#begins w/ ---- use ^
#ends w/ ------ use $

#only print the first number
print()
print('Only the first number --- ^')
numericalString = re.compile(r'^\d+')
x = numericalString.search('2343 and 23020')
print(x)

#only print the last Number
print()
print('Only the last number --- $')
numericalString = re.compile(r'\d+$')
x = numericalString.search('this is a test 2343 and 23020')
print(x)

#note ^ and $ will only work if the string contains the regex value at the END
#carets first, dollars last. carets cost dollars.

print("\n")

#Using * to take all after a certain pattern
print('Wildcard * in use to take all after certain pattern')
name = re.compile(r'First Name: (.*) Last Name: (.*)')
x = name.search('My First Name: John Last Name: smith.')
print(x.group(1,2))

#ignore case w/ re.ignoreCase or re.I
print()
print('Ignore case w/ re.ignoreCASE')
caseTest = re.compile(r'john', re.IGNORECASE)
x = caseTest.findall('Hello john JOHN, joHN, JOhn.')
print(x)
