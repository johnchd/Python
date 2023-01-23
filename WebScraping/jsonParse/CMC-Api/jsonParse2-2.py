
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib.request
import os


os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")


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


newFile = open("TEST1.txt", "a")
newFile.write(str(working))





"""
#solution from stack overflow, but it still doesnt work
import ast
inpt = "{'status': {'timestamp': '2023-01-23T00:56:06.822Z', 'error_code': 0, 'error_message': None, 'elapsed': 18, 'credit_count': 1, 'notice': None}, 'data': {'BTC': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'category': 'coin', 'description': 'Bitcoin (BTC) is a cryptocurrency . Users are able to generate BTC through the process of mining. Bitcoin has a current supply of 19,269,750. The last known price of Bitcoin is 22,756.47416387 USD and is down -0.52 over the last 24 hours. It is currently trading on 9942 active market(s) with $24,561,958,377.70 traded over the last 24 hours. More information can be found at https://bitcoin.org/.', 'slug': 'bitcoin', 'logo': 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png', 'subreddit': 'bitcoin', 'notice': '', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 'tag-names': ['Mineable', 'PoW', 'SHA-256', 'Store Of Value', 'State Channel', 'Coinbase Ventures Portfolio', 'Three Arrows Capital Portfolio', 'Polychain Capital Portfolio', 'Binance Labs Portfolio', 'Blockchain Capital Portfolio', 'BoostVC Portfolio', 'CMS Holdings Portfolio', 'DCG Portfolio', 'DragonFly Capital Portfolio', 'Electric Capital Portfolio', 'Fabric Ventures Portfolio', 'Framework Ventures Portfolio', 'Galaxy Digital Portfolio', 'Huobi Capital Portfolio', 'Alameda Research Portfolio', 'a16z Portfolio', '1Confirmation Portfolio', 'Winklevoss Capital Portfolio', 'USV Portfolio', 'Placeholder Ventures Portfolio', 'Pantera Capital Portfolio', 'Multicoin Capital Portfolio', 'Paradigm Portfolio'], 'tag-groups': ['OTHERS', 'ALGORITHM', 'ALGORITHM', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY'], 'urls': {'website': ['https://bitcoin.org/'], 'twitter': [], 'message_board': ['https://bitcointalk.org'], 'chat': [], 'facebook': [], 'explorer': ['https://blockchain.coinmarketcap.com/chain/bitcoin', 'https://blockchain.info/', 'https://live.blockcypher.com/btc/', 'https://blockchair.com/bitcoin', 'https://explorer.viabtc.com/btc'], 'reddit': ['https://reddit.com/r/bitcoin'], 'technical_doc': ['https://bitcoin.org/bitcoin.pdf'], 'source_code': ['https://github.com/bitcoin/bitcoin'], 'announcement': []}, 'platform': None, 'date_added': '2013-04-28T00:00:00.000Z', 'twitter_username': '', 'is_hidden': 0, 'date_launched': None, 'contract_address': [], 'self_reported_circulating_supply': None, 'self_reported_tags': None, 'self_reported_market_cap': None}}}{'status': {'timestamp': '2023-01-23T00:57:20.853Z', 'error_code': 0, 'error_message': None, 'elapsed': 22, 'credit_count': 1, 'notice': None}, 'data': {'BTC': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'category': 'coin', 'description': 'Bitcoin (BTC) is a cryptocurrency . Users are able to generate BTC through the process of mining. Bitcoin has a current supply of 19,269,750. The last known price of Bitcoin is 22,756.47416387 USD and is down -0.52 over the last 24 hours. It is currently trading on 9942 active market(s) with $24,561,958,377.70 traded over the last 24 hours. More information can be found at https://bitcoin.org/.', 'slug': 'bitcoin', 'logo': 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png', 'subreddit': 'bitcoin', 'notice': '', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 'tag-names': ['Mineable', 'PoW', 'SHA-256', 'Store Of Value', 'State Channel', 'Coinbase Ventures Portfolio', 'Three Arrows Capital Portfolio', 'Polychain Capital Portfolio', 'Binance Labs Portfolio', 'Blockchain Capital Portfolio', 'BoostVC Portfolio', 'CMS Holdings Portfolio', 'DCG Portfolio', 'DragonFly Capital Portfolio', 'Electric Capital Portfolio', 'Fabric Ventures Portfolio', 'Framework Ventures Portfolio', 'Galaxy Digital Portfolio', 'Huobi Capital Portfolio', 'Alameda Research Portfolio', 'a16z Portfolio', '1Confirmation Portfolio', 'Winklevoss Capital Portfolio', 'USV Portfolio', 'Placeholder Ventures Portfolio', 'Pantera Capital Portfolio', 'Multicoin Capital Portfolio', 'Paradigm Portfolio'], 'tag-groups': ['OTHERS', 'ALGORITHM', 'ALGORITHM', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY'], 'urls': {'website': ['https://bitcoin.org/'], 'twitter': [], 'message_board': ['https://bitcointalk.org'], 'chat': [], 'facebook': [], 'explorer': ['https://blockchain.coinmarketcap.com/chain/bitcoin', 'https://blockchain.info/', 'https://live.blockcypher.com/btc/', 'https://blockchair.com/bitcoin', 'https://explorer.viabtc.com/btc'], 'reddit': ['https://reddit.com/r/bitcoin'], 'technical_doc': ['https://bitcoin.org/bitcoin.pdf'], 'source_code': ['https://github.com/bitcoin/bitcoin'], 'announcement': []}, 'platform': None, 'date_added': '2013-04-28T00:00:00.000Z', 'twitter_username': '', 'is_hidden': 0, 'date_launched': None, 'contract_address': [], 'self_reported_circulating_supply': None, 'self_reported_tags': None, 'self_reported_market_cap': None}}}"
json_data = ast.literal_eval(json.dumps(inpt))
print(json_data)
#solution does not work because it still prints everything out w/ a ', and not a " - cant parse this w/ json
"""



# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
'''
{'status': {'timestamp': '2023 ---- does not work
{"status":{"timestamp":"2023  ----- works (straigt from response using burpSuite)
----
when I get the file from python, it adds in a ", throwing everything off
'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# solution :
'''
x = x.replace("'", '"')
j = json.loads(x)
'''


