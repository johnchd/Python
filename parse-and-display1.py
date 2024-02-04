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


        for req in timeOpens:
            # print(req['quote'])
            priceAnalysis = req['quote']
            # testDict[priceAnalysis] = symbol
            singlePrice = priceAnalysis['close']
            marketcap = priceAnalysis['marketCap']
        # print(singlePrice)
        # print(symbol)
        testDict[symbol] = singlePrice, marketcap
    # print(testDict)
    multipleVals1(testDict)

def multipleVals1(testDict):
    # print(testDict) #{'BTC': (23031.0897756201, 443936922524.46)}
    
    cryptosList = []
    for key, value in testDict.items():
        # print(key)
        ccName = key
        cryptosList.append(ccName)
    # print(ccNames)

    pricesList = []
    marketcapsList = []
    for key, value in testDict.items():
        # print(value) #prints both
        prices = value[0]
        pricesList.append(prices)
        marketcaps = value[1]
        marketcapsList.append(marketcaps)
    # print(marketcapsList)
    
    multipleVals2(cryptosList, pricesList, marketcapsList)

def multipleVals2(cryptosList, pricesList, marketcapsList):
    # print(cryptosList, pricesList, marketcapsList)

    newTestDict = dict(zip(cryptosList,zip(pricesList, marketcapsList)))
    # print(newTestDict)
    multipleVals3(newTestDict)


def multipleVals3(newTestDict):
    # print(newTestDict)

    cryptoNamesList = []
    allPricesList = []
    marketcapsList = []
    for key, value in newTestDict.items():
        # print(key) #btc
        cryptos = key
        cryptoNamesList.append(cryptos)
        prices = value[0]
        allPricesList.append(prices)
        marketcaps = value[1]
        marketcapsList.append(marketcaps)
        # print(value[0]) #price
        # print(value[1]) #marketcap
    # print(cryptoNamesList, allPricesList, marketcapsList)

    for cryptos, prices, marketcaps in zip(cryptoNamesList, allPricesList, marketcapsList):
        # print(cryptos, prices, marketcaps)
        print('Currency: ' + cryptos + '\tPrice: ' + str(prices) + '\tMarketcap: ' + str(marketcaps))



rawInfo()





