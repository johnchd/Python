from fileinput import filename
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib.request
import os

# os.chdir("/Users/john/Desktop/<path>")


#Auth to CMC's API
#Part 1 - Hit CMC API, get response, and place into dict (parseResponse)
#Part 2 - Put symbols into list (First 2 (btc, eth))
#Part 3 - Insert the Symbols from list into URL
#Part 4 - Get each response / insert into variable, then parse


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<api-key>',
}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print()
print('Part 1 --- Auth to CMC ')
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
print('Part 3 - List of SYMBOLS appended to URL: ')          
test1 = [] 
for symbol in nameList:
    urlList = []
    urlSymbol = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}'.format(symbol)
    urlList.append(urlSymbol)
    print(urlList)

    #Part 4 - Get each response / insert into variable, then parse
    for url in urlList:
        req = requests.get(url, headers=headers)
        #print(req)
        allResponses = req.content
        parseResponse = json.loads(allResponses)
        readAll = json.dumps(parseResponse)
        test1.append(readAll)
#print(test1)

print()
print('Part 4 --- Extracting the Symbol / ID from response:')
for response in test1:
    #print(response) #works
    test1_to_dict = json.loads(response)

    #Best way:
    for key, value in test1_to_dict['data'].items():
        print(key, value['description'])



