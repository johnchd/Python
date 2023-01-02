#!/usr/bin/env python3

import re

#search() vs findall() w/ pipe
print()
print('Here is a pipe along w/ search() vs findall()')
testRegex = re.compile(r'bugbounty|hacking')
x = testRegex.findall('This is a testttt bugbounty, test hacking.')
#print(x.group()) #use w/ testRegex.search()
print(x) #use w/ testRegex.findall()

#further use of pipe
#You can also use the pipe to match one of several patterns as part of your regex.
print()
print('Here is a pipe in use: ')
testRegex = re.compile(r'test(ing|ed|er|)')
x = testRegex.search('I am a tester that does testing and I tested this.')
print(x.group(0))

#optinal matching w/ question mark ---- batman or batwoman --> OPTIONAL
print()
print('Here is a ? in use:')
moreReg = re.compile('bat(wo)?man')
x = moreReg.search('this is a test for batwoman') 
print(x.group())

#matching zero or more with ***** --- can be any amount of wowowo
print()
print('Here is a * in use:')
anotherOne = re.compile('bat(wo)*man')
x = anotherOne.search('batwowowowowoman')
print(x.group())

#matching w/ one or more plus's (+)
print()
#the group preceding a plus must appear at least once
print('Here is a + sign in use:')
thePlus = re.compile('bat(wo)+man')
x = thePlus.search('i am a batmomomoman')
print(x)

#match specific patterns w/ braces {}
print()
print('Here is an example of the {} in use: ')
braces = re.compile('(ha){3}')
x = braces.search('Here are are at last hahahahah lets see this.')
print(x)



print()






