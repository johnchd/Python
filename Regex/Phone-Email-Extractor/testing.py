#!/usr/bin/python3

#steps
    #1 - create email regex
    #2 - create phone regex
    #3 - put it all together

import re

#Part 1 - EmailRegex
emailRegex = re.compile(r'''(
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- jcrynick
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    )''', re.VERBOSE)

test = emailRegex.findall('Hello this tesdfasdf@icloud.com a test for asdfasdf@gmail.com Regex.')
#print(test) #ensure it prints out email
for i in test:
    print(i)


#Part 2 - PhoneNumber regex
phoneRegex = re.compile(r'''(
                                      #? matches zero or one of the preceding group
    ( \d{3} | \(\d{3}\) )             # area code --- 440 or (440)
    ( \s|-|\. ) ?                     # separator - any space | - | . 
    ( \d{3} )                         # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    
    )''', re.VERBOSE)

test1 = phoneRegex.findall('test 4 jc 440-759-2334, 404.330-3030, (494)-340-3033')
#print(test1) #ensure it prints out number
print()
for i in test1:
    print(i[0])