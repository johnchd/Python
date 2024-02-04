#!/usr/bin/python3

import os

#see all contents of a Directory
for folderName, subFolders, fileNames in os.walk('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files'):
    print('The folder name is: ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filneames in ' + folderName + ' are: ' + str(fileNames) + ' \n')


#get current directory
directory = os.getcwd()
print('Current directory ---- ' + directory)

"""
print()
for folderName in os.walk('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files'):
    print(folderName)
"""

#create files
for file in range(3):
    file = open(f'testFile{file + 1}.txt', 'w') #creates 3 files named test# file (1,2,3)


#baconFile = open('bacon.txt', 'w')   
#baconFile.write('Hello, world!\n')



