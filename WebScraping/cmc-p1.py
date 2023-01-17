#!/usr/bin/python3

#Script to scrape CMC's api and retrieve only name/price
#Must have account to generate API key

#Step 1 - Hit cmc's api successfully and confirm 200 response - good
#Step 2 - Download first 10 currencies information to file (name file) - good
#Step 3 - Open file and use RegEx to parse the data to retrieve only Name/Price
#Step 4 - copy info to clipboard w/ pyperclip

import requests
from requests.auth import HTTPBasicAuth
import urllib.request


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<api-key>',
}

req = requests.get(url, headers=headers)


#this gets the ALL the contents of a response
x = req.content
#print(x)

#create new file
newFile = open("cmcInfo.txt", "a")
newFile.write(str(x))



