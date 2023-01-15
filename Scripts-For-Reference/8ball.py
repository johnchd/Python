#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:38:39 2022

@author: john
"""

import random

def test(spam):
    if spam == 1:
        return 'cool'
    elif spam == 2:
        return 'test123'
    elif spam==3:
        return 'ymca'
    elif spam == 4:
        return 'stairmaster'
    
r = random.randint(0,4)
y = test(r)
print(y)


