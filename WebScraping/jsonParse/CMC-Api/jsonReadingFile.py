#parse info out of json file
import os
import json

os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse/Generated-Files")


'''
#PART 1
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")
with open('TEST1.txt') as f:
    json_data = json.load(f)

#### actually works
print(type(json_data)) ###<class 'dict'>
#print(json_data)
print(json_data['data']['BTC']['id'])

#print(json_data) #works but notice the single quote ' --- (test w/ TEST1.txt)
#print(json.dumps(json_data)) # works GREAT, putting it in variable for ease of use
test_dict = json.dumps(json_data)
'''



#PART 2 - parsing DBL quotes does not work
'''
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")
with open('jsonParse2-dblQuote.txt') as f:
    json_data = json.load(f)

#### cant even parse the JSON when it has 2 quotes
print(type(json_data)) ###<class 'dict'>
#print(json_data)
#print(json_data['data']['BTC']['id'])
'''

#PART 3 - parsing SINGLE quotes ???? still doesnt work
'''
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")
with open('jsonParse2-singleQuote.txt') as f:
    json_data = json.load(f)

#### cant even parse the JSON when it has 2 quotes
print(type(json_data)) ###<class 'dict'>
#print(json_data)
#print(json_data['data']['BTC']['id'])
'''


#part 4 - Think I have to split each line after status
'''
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")
with open('jsonParse2.txt') as f:
    json_data = json.load(f)

print(json_data)
'''

#part 5 -- stack overflow --- works but looking for better solution
'''

items = []
with open('jsonParse2.txt') as f: #jsonParse2-3-test.txt (testPOC)
    for line in f:
        items.append(json.loads(line))

print(items[1])
'''

#need to parse jsonParse2.txt and have it as so:
'''
status:
status:
status:
    instead of:
        status: .... status: .... status: ....

'''

#part 6 -- stack overflow --- works but looking for better solution




os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse/Generated-Files")
with open('CMC-Final-Show.txt') as f:
    json_data = json.load(f)

print(json_data)