#!/usr/bin/python3
import os, glob, re

#find emails/phone numbers in TXT file

#Part 1 - regex
emailRegex = re.compile(r'''(
    #email
    \w+[a-zA-Z0-9+-_.]  #part 1 of email --- email
    @                   #part 2 of email --- @
    \w+[a-zA-Z0-9]      #part 3 of email --- gmail
    .                   #part 4 of email --- .
    \w+[a-zA_Z0-9]      #part 5 of email --- com
    

    )''', re.VERBOSE)

phoneRegex = re.compile(r'''(
    #phone
    ( \d{3} | \(\d{3}\) )             # area code --- 440 or (440)
    ( \s|-|\. ) ?                     # separator - any space | - | . 
    ( \d{3} )                         # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension

    )''', re.VERBOSE)

#Part 2 - specify the path
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/RW-Files/testing")

path = "/Users/john/Desktop/GoogleDrive/ATBS/RW-Files/testing"
dir_list = os.listdir(path)
print('Files in specified path:\n ' + str(dir_list))

#Part 3 - find expressions in all txt files
print()
for file in glob.glob('*txt'):
    print('\n' + file) #prints only file names
    openFile = open(file)
    readFile = openFile.read()
    #print(readFile) #prints out all contents of specified files
    #regexed.re(readFile)

    parse = readFile
    email = emailRegex.findall(parse)
    phone = phoneRegex.findall(parse)
    #print(email)
    print('\n'.join(email))


    for i in phone:
        print(i[0])

#it  does not appear python can read/open pdf files without a module like pdfminer.six
#i believe this will work with any text based file like: csv, xls, txt, py, type 

################


