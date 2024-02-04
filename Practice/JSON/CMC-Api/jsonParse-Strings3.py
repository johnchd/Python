
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib.request
import os


os.chdir("/Users/john/Desktop/<path>")


urlSymbol = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol=BTC'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<api-key>',
}


#works but theres a problem

req = requests.get(urlSymbol, headers=headers)
#this gets the ALL the contents of a response
allResponses = req.content
parseResponse1 = json.loads(allResponses)
#print(parseResponse1)
working = json.dumps(parseResponse1) ###this solves it all


# newFile = open("TEST1.txt", "a")
# newFile.write(str(working))





