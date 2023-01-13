#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:13:47 2022

@author: john
"""

spam = ['apples', 'bananas', 'tofu', 'cats']

#print(spam[-1]) #---test to get last item of list

lastVar = spam[-1]
print(lastVar) #---grabbed last item w/ -1

print('and ' + lastVar) #---trying to add to end of spam

spam.insert(-1, 'and') #adds it into list as string
print(spam)

lastVar = spam[-1]
print(lastVar) # cats
print(lastVar[0]) # c

print(lastVar + ' and ' + str([0])) #wrong - cats and [0]

print(' and ' + lastVar) #  and cats
x = ('and ' + lastVar)

print(x)

spam.append(x)
print(spam)


#000-303-3030