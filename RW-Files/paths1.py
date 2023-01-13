#!/usr/bin/python3

from pathlib import Path
import os


#using path files
x = Path('spam', 'bacon', 'eggs')
print(x)

print()
print('Modify files with the path module:')
x = Path('C://Users/John/') / 'bacon' / 'eggs'
print(x)

print()
x =Path('spam') / Path('bacon/eggs')
print(x)

print()
print('Print current working dir w/ path.cwd: ')
x = Path.cwd()
print(x)

print()
print('Print home dir w/ path.home:')
x = Path.home()
print(x)

#create directory
#os.makedirs('/Users/john/Desktop/test4jc')

p = Path('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files')
print(p.parent) #anchor, parent, name, stem, suffix, drive





