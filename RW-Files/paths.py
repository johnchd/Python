#!/usr/bin/python3

from pathlib import Path
import os

print('List files in Directory:')
# Get the list of all files and directories
path = "/Users/john/Desktop/GoogleDrive/ATBS/Regex"
dir_list = os.listdir(path)

# prints all files
print(dir_list)

#pathAndFile = "/Users/john/Desktop/GoogleDrive/ATBS/Regex/reg.py"



print()
pathToFile = "/Users/john/Desktop/GoogleDrive/ATBS/Regex/reg.py"
#seperate the path / file
print('Seperated path and file: ')
print(os.path.split(pathToFile))
print('Only the basename: ')
print(os.path.basename(pathToFile))

print()
print('Seperate all w/ os.sep:')
x = path.split(os.sep)
print(x)

#get all files w/ glob
"""
print()
p = Path('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files')
print(list(p.glob('*.py')))
"""


newFile = open('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files/paths.py')
print(newFile.read())



