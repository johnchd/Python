#!/usr/bin/python3

import requests

x = requests.get('https://coinmarketcap.com/')

#this just gets all the source code
#would be better off hitting the API
print('Source code: ' + x.text[:15])

print('Status code: ' + str(x.status_code))