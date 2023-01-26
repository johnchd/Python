from fileinput import filename
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib.request
import os

os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse/Generated-Files")


#Auth to CMC's API
#Part 1 - Hit CMC API, get response, and place into dict (parseResponse)
#Part 2 - Put symbols into list (First 3 (btc, eth, USD))
#Part 3 - Insert the 3 Symbols from list into URL
#Part 4 - Go to each url within (urlList), get responses, and combine into file
#Part 5



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e12fc04a-ac13-4f7f-8e83-9cd3a2d2f43e',
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
print()
urlList = []
print('Part 3 - List of SYMBOLS appended to URL: ')
for slug in nameList:
    urlSymbol = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}'.format(slug)
    urlList.append(urlSymbol)
print(urlList)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#Part 4 - Go to each url within (urlList), get response, and grab "ID"
    #EX:
        #"data":{"BITCOIN":{"id":15907...
print()
for url in urlList:
    req = requests.get(url, headers=headers)
    #this gets the ALL the contents of a response
    allResponses = req.content
    parseResponse1 = json.loads(allResponses)
    readAll = json.dumps(parseResponse1)

    print(readAll)
    #print(parseResponse1) ####works, but makes it using single quote - cant parse single quote json
    #instead use json.dumps(data), this makes it w/ double quote, allowing ability to parse


    #print it to file for ease of working (maybe better anyway)
    

    #method 1
    #newFile = open("CMC-Final-Show.txt", "a") #method 1
    #newFile.write(str(readAll))
    






