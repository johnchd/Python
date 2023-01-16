#!/usr/bin/python3

import os, glob, shutil

#Selective Copy

#Program that walks through a folder tree and searches for files 
#with a certain file extension (such as .pdf or .jpg). 
#Copy these files from whatever location they are in to a new folder.



'''
for folderName, subFolders, fileNames in os.walk('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files'):
    print('The folder name is: ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filneames in ' + folderName + ' are: ' + str(fileNames) + ' \n')
'''

#part 1
#simple for loop to find all specific files within a directory
'''
for folderName, subFolders, fileNames in os.walk('/Users/john/Desktop/GoogleDrive/ATBS/RW-Files'):
    for files in fileNames: 
        #print(files)

        if files.endswith('.py'):
            #print(files)
            print(os.path.join(folderName, files))
'''

for folderName, subFolders, fileNames in os.walk('/Users/john/Desktop/GoogleDrive/ATBS'):
    for files in fileNames: 
        #print(files)

        if files.endswith('.py'):
            #print(files)
            #print(os.path.join(folderName, files))
            x = os.path.join(folderName, files)
            

            #create directory
            os.makedirs('/Users/john/Desktop/GoogleDrive/ATBS/createdDir', exist_ok=True)
            
          
            #copy to directory
            shutil.copy2(x, '/Users/john/Desktop/GoogleDrive/ATBS/createdDir')



