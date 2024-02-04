#!/usr/bin/python3

#Program that analyzes clipboard information and finds PII such as emails/phone numbers
#All output will be output into the terminal, and copied back into clipboard

#Steps
    #1 - Create email regex
    #2 - Create phone regex
    #3 - Put it all together

import re, pyperclip

#Part 1 - EmailRegex
emailRegex = re.compile(r'''(
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- email
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    )''', re.VERBOSE)


#Part 2 - PhoneNumber regex
phoneRegex = re.compile(r'''(
                                      #? matches zero or one of the preceding group
    ( \d{3} | \(\d{3}\) )             # area code --- 440 or (440)
    ( \s|-|\. ) ?                     # separator - (space OR hypen OR period)
    ( \d{3} )                         # first 3 digits
    (\s|-|\.)                         # separator - (space OR hypen OR period)
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension - anything after space, ext OR x OR ext. and then anything after a SPACE/TAB/NewLine Char thats 2-5 digits long
    )''', re.VERBOSE)

#Part 3 - Putting it all together
data = pyperclip.paste()

#email
test = emailRegex.findall(data)
foundEmails = "\n".join(test) #works

#phone
test1 = phoneRegex.findall(data) #put string in here to test
newList = [f"{i[0]}" for i in test1]
foundNumbers = "\n".join(newList)

#together
extractedData = foundEmails + '\n' + foundNumbers
print('Copied to clipboard: ' + '\n' + extractedData)
pyperclip.copy(extractedData)



"""
afsdfasd
afsdf
a
sdf
asdf
email@email.com
ead 440-390-3940 fadsf emailing@email.com
adf
440 999 0000 adffsd gmailing@gmail.com
testing
fasdfasdfadsf
email@icloud.com
adfasdf
a
sdf

"""
