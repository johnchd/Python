#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:53:11 2022

@author: john
"""

# DICTIONARIES - PART 1
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
testing = {'rope': 10, 'torch': 6000, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print('   ' + str(v) + ' ' + str(k) + "'s")
        
        
    print()
    print('Total inventory: ')
    x = sum(inventory.values()) 
    print(x)

displayInventory(stuff)

print()
print()
print()

#
#
#
#List to Dictionary Function

#LISTS - PART 2
dragonLoot = ['gold coin', 'dagger','dagger','dagger', 'gold coin', 'gold coin','gold coin','gold coin','gold coin','gold coin','gold coin', 'ruby']

#inventory below
testingINV = {'gold coin': 0, 'dagger': 0}

#the LIST (dragonLoot) should be ADDED to the DICTIONARY testingINV
#this should be done via function

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        inventory[loot] = inventory[loot] + 1
    return(inventory)
        

testingINV = addToInventory(testingINV, dragonLoot)
displayInventory(testingINV)





















