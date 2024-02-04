#!/usr/bin/python3

import re,pyperclip

#Part 1 - make sure regEx works w/ string
"""
#Part 1 - EmailRegex
emailRegex = re.compile(r'''(
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- email
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    )''', re.VERBOSE)

test = emailRegex.findall('Hello this jcrynick@icloud.com a test for jcrynick@gmail.com Regex.')
#print(test) #ensure it prints out email
for i in test:
    print(i)
"""

#Part 2 - copy information then run this script to output info to terminal
"""
emailRegex = re.compile(r'''(
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- email
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    )''', re.VERBOSE)

findEmail = pyperclip.paste()

test = emailRegex.findall(findEmail)
#print(test) #ensure it prints out email
for i in test:
    print(i)

"""

#Part 3 - Final working - copy information then run this script to output info to clipboard.
#so instead one can just paste right into document of their choice
#ideally this goes directly into file - but I am not there yet 

emailRegex = re.compile(r'''(
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- email
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    )''', re.VERBOSE)

findEmail = pyperclip.paste()

test = emailRegex.findall(findEmail)
#print(test) #ensure it prints out email
x = "\n".join(test)
print('copied to clipboard: \n' + x)
pyperclip.copy(x)



#Part 3.1 - copy() module only copied the last item
#many things were tried, but I could not get this to work
#the copy() module would only copy the last value
    #i found that joining the lines together, and THEN using the copy() module, I was successful
"""
emailRegex = re.compile(r'''(
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- email
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    )''', re.VERBOSE)

findEmail = pyperclip.paste()

test = emailRegex.findall(findEmail)
#print(test) #ensure it prints out email

for i in test:
    pyperclip.copy(i)
"""

