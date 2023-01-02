#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:08:46 2022

@author: john
"""

tools = ['burp', 'intruder', 'repeater', 'msfvenom', 'comparer']
for i in range(len(tools)):
    print('Index: ' + str(i) + ' is ' + tools[i])
    

print()
tools = ['burp', 'intruder', 'repeater', 'msfvenom', 'comparer2']
for index, item in enumerate(tools):
    print('Index: ' + str(index) + ' is ' + item)



#run the current cell to see the difference
    #range(len(list))
    #enumerate(list)
        #both do the same thing

