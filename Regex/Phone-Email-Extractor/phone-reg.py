#!/usr/bin/python3

import re,pyperclip

#Part 1 - PhoneNumber regex
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
#print(test1) #Part 1 - ensure it prints out number

new = [f"{i[0]}" for i in test1]

#print(new) #test to make sure it prints out numbers. They are printed in list, which is not good for display

x = "\n".join(new)

print()
print('copied to clipboard: \n' + x)
pyperclip.copy(x)




#again the below for loop only copies the LAST item, so the lines must be joined together to work
"""
for i in test1:
    print(i[0])
    pyperclip.copy(i[0])
"""













