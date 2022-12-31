#!/usr/bin/env python3

#count chars in string
string = "the "
count = 0 
   
#Counts each character except space  
for i in range(0, len(string)):  
    #if(string[i] != ' '): #dont count spaces 
    count = count + 1   
print("Characters in string: " + str(count))


#counts items in list
testList = ['test', 'for', 'jc']
itemCounter = 0

for i in range(0, len(testList)):
    itemCounter = itemCounter + 1
print("Items in list: " + str(itemCounter))

#print items in list
print()
print("Printing ITEMS in list w/ FOR loop: ")
for x in testList:
    print("   test: " + x)

#indexing
print()
print('Indexing w/ FOR loop & range(len()')
for x in range(len(testList)):
    print("   " + str(x))


#Items and Position in list using ENUMERATE
print()
print('Iemizing list w/ ENUMERATE()')
testList1 = ['test', 'for', 'jc']
for index,y in enumerate(testList1):
    print(str(index) + ' - ' + y)

#items and positions in list using FOR loop
print()
print('Itemizing list w/ FOR loop:')
testList2 = ['test', 'for', 'jc','two']
for i in range(len(testList2)):
    print(str(i) + ' - ' + testList2[i])



#Items and Position in NESTED list
print()
testList2 = [['test', 'for', 'jc'], ['cool', 'fkin', 'beans','lol']]
testing = ['test', 'for', 'jc','two']

for i in range(len(testList2)):
    x = testList2[i]
    
    print()
    for index,y in enumerate(x):
        print(index,y)

    

       

