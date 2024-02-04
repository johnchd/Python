#!/usr/bin/python3

#steps
    #1 - create email regex
    #2 - create phone regex
    #3 - put it all together

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








#prints out all data I want but need to COPY the data
#all works here, still have to copy the data
"""
#email
findEmail = pyperclip.paste()
test = emailRegex.findall(findEmail)
foundEmails = "\n".join(test) #works
print(foundEmails)


#phone
findPhone = pyperclip.paste()
test1 = phoneRegex.findall(findPhone) #put string in here to test
newList = [f"{i[0]}" for i in test1]
foundNumbers = "\n".join(newList)
print(foundNumbers)
"""


#works great - clean up var names -  working
"""
#email
findEmail = pyperclip.paste()
test = emailRegex.findall(findEmail)
foundEmails = "\n".join(test) #works
#print(foundEmails)


#phone
findPhone = pyperclip.paste()
test1 = phoneRegex.findall(findPhone) #put string in here to test
newList = [f"{i[0]}" for i in test1]
foundNumbers = "\n".join(newList)
#print(foundNumbers)

xyz = foundEmails + '\n' + foundNumbers
print(xyz)
pyperclip.copy(xyz)
"""



#final iteration
"""
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
print(extractedData)
pyperclip.copy(extractedData)
"""






"""
#Part 1 - EmailRegex
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
foundEmails = "\n".join(test) #works
print('copied to clipboard: \n' + foundEmails)
#pyperclip.copy(foundEmails) #works


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

findPhone = pyperclip.paste()

test1 = phoneRegex.findall(findPhone) #put string in here to test

newList = [f"{i[0]}" for i in test1]
foundNumbers = "\n".join(newList)


print()
print(foundNumbers)
#pyperclip.copy(foundNumbers)

#prints out all data I want but need to COPY the data
"""





