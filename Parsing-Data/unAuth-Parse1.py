import json
import requests



def rawInfo():
    rawInfoList = []
    for i in range(1, 5):
        currencies = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={}&convertId=2781&timeStart=1674861000&timeEnd=1674867600".format(i)
        req = requests.get(currencies)
        allResponses = req.content
        allData = json.loads(allResponses)
        # print(allData) #this prints out 5 dictionaries
        rawInfoList.append(allData)
    # print(rawInfoList)
    symbol_and_price(rawInfoList)


def symbol_and_price(rawInfoList):
    testDict = {}
    for req in rawInfoList:
        # print(req) #<class 'dict'>
        # print(req['data']['symbol']) #btc/ltc/etc
        symbol = req['data']['symbol']
        # timeOpens = req['data']['quotes'] # lists
        timeOpens = req['data']['quotes'] # lists
        # print(timeOpens[0]['timeOpen']) # works
        ccID = req['data']['id']
        # print(ccID)


        for req in timeOpens:
            # print(req['quote'])
            priceAnalysis = req['quote']
            # testDict[priceAnalysis] = symbol
            singlePrice = priceAnalysis['close']
            marketcap = priceAnalysis['marketCap']
        # print(singlePrice)
        # print(symbol)
        # testDict[symbol] = singlePrice, marketcap #outputs SET - {'BTC': (23031.0897756201, 443936922524.46)}
        testDict[symbol] = [singlePrice, marketcap, ccID] #outputs LIST - {'BTC': [23031.0897756201, 443936922524.46]}
    print(testDict)



rawInfo()
