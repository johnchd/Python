import json
import requests
from requests.auth import HTTPBasicAuth



#Auth to CMC's API
#Part 1 - Hit CMC API, get response, and place into dict (parseResponse)
# Part 1.1 - Begin to extract data out of the raw JSON
#Part 2 - Put symbols into list (First 3 (btc, eth)
#Part 3 - Insert the 2 Symbols from list into URL
#Part 4 - Go to each url within (urlList) and get responses



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<api-key>',
}

# Part 1 - Authenticate, hit CMC API, get response, and place into dict (parseResponse)
req = requests.get(url, headers=headers)
response = req.content
parseResponse = json.loads(response) 
# print(parseResponse) #print out raw JSON
# print(type(parseResponse)) # <class 'dict'>

# Part 1.1 - Begin to extract data out of the raw JSON
# for i in parseResponse:
#     print(i) #status, data




# #Part 2 - Put symbols into list
nameList = []
# #prints all symbols AND adds to list
# print()
for name in parseResponse['data']:
    # print(name['name']) #id, name, symbol, slug, etc
    nameList.append(name['symbol'])
print('Part 2 --- List of symbols:\n' + str(nameList))


# Part 3 - Insert Symbols from list into URL
#https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}
print()
urlList = []
print('Part 3 - List of SYMBOLS appended to URL: ')
for slug in nameList:
    urlSymbol = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}'.format(slug)
    urlList.append(urlSymbol)
print(urlList)

#Part 4 - Go to each url within (urlList), get response, and grab "ID"
print()
for url in urlList:
    req = requests.get(url, headers=headers)
    #this gets the ALL the contents of a response
    allResponses = req.content
    parseResponse1 = json.loads(allResponses)
    readAll = json.dumps(parseResponse1)
    print("\n")

    print(readAll)

    
