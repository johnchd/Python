#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:35:14 2022

@author: john
"""

message = 'aaaaaaaaaaa ffffffffddddddddd ooooooo'
count = {}


for chars in message:
    count.setdefault(chars, 0)
    count[chars] = count[chars] + 1
    
print(count)

spam = '12 456'
print(spam)

x = spam.split()
print(x)