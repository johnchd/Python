#!/usr/bin/python3

import os

#get current directory
currentDir = os.getcwd()
print('Current Directory ---- ' + currentDir)

print()
os.chdir('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files/testing')
print('New Current Directory ---- ' + os.getcwd())
#print('Current directory ---- ' + currentDir)


