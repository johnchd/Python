import json
from time import strftime
import requests
from datetime import datetime, date
import datetime as dt
import re



url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1014694800&timeEnd=1674867600'


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print()
#PART 1 - Hit CMC API, retrieve all BTC historical price data
req = requests.get(url)
#this gets the ALL the BTC data
btcResponse = req.content
btcData = json.loads(btcResponse)
#print(btcAnalysis)
#print(type(btcAnalysis)) ##<class 'dict'>



priceAnalysis = btcData['data']['quotes']
# print(type(priceAnalysis[0:])) #<class 'list'>
# print(priceAnalysis[0:]) #<class 'list'>
x = priceAnalysis[0:]



#works, part 1
# for allQuotes in x:
#     #print((allQuotes)) #<class 'dict'> -- #prints open, high, low, close, volume, marketcap, timestamp
#     #print(allQuotes['timeOpen'])

#     for key in allQuotes.values():
#         print(key)
    
#part 2 - retrieve closing price along with timestamp, and insert into list
closingPrices = []
timestamp = []
for allQuotes in x:
    # print(allQuotes) #<class 'dict'> -- #prints open, high, low, close, volume, marketcap, timestamp
    # print(allQuotes['quote']['close'])
    closingPrices.append(allQuotes['quote']['close'])
    timestamp.append(allQuotes['quote']['timestamp'])
#print(closingPrices)
#print(closingPrices)


#part 3 - format time for easier reading
newTimeStamp = []
for date in timestamp:
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ').date()
    #print(type(date_object)) #<class 'datetime.date'>
    newDate_object = str(date_object)
    newTimeStamp.append(newDate_object)
#print((newTimeStamp))


# # # # METHOD 1 # # # # # 
# #part 4.1 - combine closing price / timestamp into list and zip
# for time, price in zip(newTimeStamp, closingPrices):
#     #print(time + ' - ' +  str(price))
#     print(time + ' - ' +  str(price))
#     ### OR ###

# #part 5.1 - use regex to query for price analysis based on year, quarter, month, etc
# r = re.compile("2013")
# test = list(filter(r.match, newTimeStamp)) # Read Note below
# print(test)




# # # # METHOD 2 # # # # # 
zipped = zip(newTimeStamp, closingPrices)
zippedDict = dict(zipped)
# print(zipped)

#print(zippedDict)

zippedDictLIST = []
for time, price in zippedDict.items():
    # print(time + ' - ' + str(price))
    zippedDict2str = (time + ' - ' + str(price))
    #print((zippedDict2str)) #<class 'str'>
    zippedDictLIST.append(zippedDict2str)
#print(zippedDictLIST)


q1 = "2020-01|2020-02|2020-03"
q2 = "2020-04|2020-05|2020-06"

yearly = "\d\d\d\d-03-0"


r = re.compile(yearly)
test = list(filter(r.match, zippedDictLIST)) 
#print(test)
for i in test:
    print(i)



#Date To String Python using strftime()
#Strptime python is used to convert string to datetime object.
# # # # Solution Start # # # # #
# timestamp = ['2014-02-03T23:59:59.999Z', '2015-02-03T23:59:59.999Z']
# newTimeStamp = []
# for date in timestamp:
#     date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ').date()
#     #print(type(date_object)) #<class 'datetime.date'>
#     new = str(date_object)
#     newTimeStamp.append(new)
# print(newTimeStamp)
# # # # Solution End # # # # #



# # # # Practice Start # # # # #
# timestamp = ['2014-02-03T23:59:59.999Z', '2015-02-03T23:59:59.999Z']
# newTimeStamp = []
# for date in range(len(timestamp)):
#     date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ').date()
#     #print(type(date_object)) #<class 'datetime.date'>
#     #print(date_object)
#     newTimeStamp.append((date_object))
# print(strftime(newTimeStamp))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#g2g for practice
# from datetime import datetime, date
# practice = '2014-02-03T23:59:59.999Z'
# date_object = datetime.strptime(practice, '%Y-%m-%dT%H:%M:%S.%fZ').date() 
# print(date_object)
# #'%Y-%d-%mT%H:%M:%S.%fZ'
# # # # Practice End # # # # #







