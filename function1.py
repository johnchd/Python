import json
import requests



#method 1
# for i in range(1, 5):
#     currencies = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={}&convertId=2781&timeStart=1674867500&timeEnd=1674867600".format(i)
    

#     def GetCurrencyInfo(url):
#         global btcData
#         req = requests.get(url)
#         btcResponse = req.content
#         btcData = json.loads(btcResponse)
#         print(btcData)
#         # return btcData
#     GetCurrencyInfo(currencies)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #method 2 - works
# def main():
#     for i in range(1, 5):
#         currencies = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={}&convertId=2781&timeStart=1674867500&timeEnd=1674867600".format(i)
        

#         def GetCurrencyInfo(url):
#             req = requests.get(url)
#             global btcData
#             allResponses = req.content
#             btcData = json.loads(allResponses)
#             print(btcData)
#             # return btcData
#         GetCurrencyInfo(currencies)
# main()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



#method 3 - works
def main():
    for i in range(1, 5):
        currencies = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={}&convertId=2781&timeStart=1674867500&timeEnd=1674867600".format(i)
        

        def GetCurrencyInfo(url):
            req = requests.get(url)
            global btcData
            allResponses = req.content
            btcData = json.loads(allResponses)
            # print(btcData)
            # return btcData
        # GetCurrencyInfo(currencies)
        x = GetCurrencyInfo(currencies)

        
        def moreInfo(test):
            # testDict = {}
            # priceAnalysisKey = btcData['data']['symbol']
            priceAnalysisValue = btcData['data']['symbol']
            print(priceAnalysisValue) #BTC
            # testDict[priceAnalysisKey] = priceAnalysisValue
            # print(testDict)
        moreInfo(x)

main()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# def main():
    
#     def testing():
#         for i in range(1, 5):
#             currencies = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={}&convertId=2781&timeStart=1674867500&timeEnd=1674867600".format(i)
#             # print(currencies)
#             return currencies
#             print(currencies)


#         # def GetCurrencyInfo(url):
#         #     req = requests.get(url)
#         #     allResponses = req.content
#         #     allData = json.loads(allResponses)
#         #     print(allData)
#         #     # return btcData
#         # GetCurrencyInfo(currencies)
# main()



            # def moreInfo(test):
            #     priceAnalysis = btcData['data']['symbol']
            #     print(priceAnalysis) #BTC
            # moreInfo(x)






