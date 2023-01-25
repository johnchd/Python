from fileinput import filename
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib.request
import os

os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse/Generated-Files")


#Auth to CMC's API
#Part 1 - Hit CMC API, get response, and place into dict (parseResponse)
#Part 2 - Put symbols into list (First 2 (btc, eth))
#Part 3 - Insert the Symbols from list into URL
#Part 4 - Go to each url within (urlList), put seperate responses into 1 list
#Part 5



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<API-KEY>',
}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#PART 1 - Hit CMC API, get response, and place into dict (parseResponse)
req = requests.get(url, headers=headers)
#this gets the ALL the contents of a response
response = req.content
parseResponse = json.loads(response) ######print(type(parse)) --- <class 'dict'>


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#Part 2 - Put symbols into list
nameList = []
#prints all symbols AND adds to list
print()
for name in parseResponse['data']:
    #print(name['name']) #id, name, symbol, slug, etc
    nameList.append(name['symbol'])
print('Part 2 --- List of symbols:\n' + str(nameList))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#Part 3 - Insert Symbols from list into URL
#https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}

'''
print()
print('Part 3 - List of SYMBOLS appended to URL: ')
for symbol in nameList:
    urlList = []
    urlSymbol = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}'.format(symbol)
    urlList.append(urlSymbol)
    #print(urlList)

    
    for url in urlList:
        req = requests.get(url, headers=headers)
        #this gets the ALL the contents of a response
        allResponses = req.content
        parseResponse1 = json.loads(allResponses)
        readAll = json.dumps(parseResponse1)
        print(readAll)
'''

print()
#print('Part 3 - List of SYMBOLS appended to URL: ')
test1 = [] 
for symbol in nameList:
    urlList = []
    urlSymbol = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}'.format(symbol)
    urlList.append(urlSymbol)
    #print(urlList)

    #part 4 - get each response and put it into a variable... 
    for url in urlList:
        req = requests.get(url, headers=headers)
        #print(req)
        allResponses = req.content
        #print(allResponses)
        test1.append(allResponses)
print(test1[0])
        #print(type(test))
        #for i in test:
            #print(i)





        #for response in req:
            #test = []
            #response = req.content
            #print(response)
            #test.append(response)
            #print(response)
            #test.append(allResponses)

        
        #print(test)
        #this gets the ALL the contents of a response
        #allResponses = req.content
        #print(allResponses)
           
        
        
            #test.append(i)
        
        
 
        
    
    






