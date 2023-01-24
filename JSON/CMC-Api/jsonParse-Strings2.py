import json
import os
import json5


# JSON string
#info_symbol = '{"status":{"timestamp":"2023-01-21T15:18:43.937Z","error_code":0,"error_message":null,"elapsed":21,"credit_count":1,"notice":null},"data":{"BITCOIN":{"id":15907,"name":"HarryPotterObamaSonic10Inu","symbol":"BITCOIN"}}}'
info_symbol = '{"status":{"timestamp":"2023-01-21T15:18:43.937Z","error_code":0,"error_message":null,"elapsed":21,"credit_count":1,"notice":null},"data":{"BITCOIN":{"id":15907,"name":"HarryPotterObamaSonic10Inu","symbol":"BITCOIN","category":"token","description":"HarryPotterObamaSonic10Inu (BITCOIN) is a cryptocurrency launched in 2021and operates on the BNB Smart Chain (BEP20) platform. HarryPotterObamaSonic10Inu has a current supply of 1,000,000,000,000,000 with 0 in circulation. The last known price of HarryPotterObamaSonic10Inu is 0 USD and is up 4.98 over the last 24 hours. It is currently trading on 3 active market(s) with $0.00 traded over the last 24 hours. More information can be found at https://www.hpos10i.com.","slug":"harrypotterobamasonic10inu","logo":"https://s2.coinmarketcap.com/static/img/coins/64x64/15907.png","subreddit":"hpos10i","notice":"","tags":null,"tag-names":null,"tag-groups":null,"urls":{"website":["https://www.hpos10i.com","https://hpos10i.shop"],"twitter":["https://twitter.com/hpos10idotcom"],"message_board":[],"chat":["https://t.me/hpos10idotcom","https://discord.gg/rU3kgm5u"],"facebook":[],"explorer":["https://bscscan.com/address/0x4c769928971548eb71a3392eaf66bedc8bef4b80"],"reddit":["https://reddit.com/r/hpos10i"],"technical_doc":[],"source_code":[],"announcement":[]},"platform":{"id":"1839","name":"BNB","slug":"bnb","symbol":"BNB","token_address":"0x4c769928971548eb71a3392eaf66bedc8bef4b80"},"date_added":"2021-12-10T07:52:20.000Z","twitter_username":"hpos10idotcom","is_hidden":0,"date_launched":"2021-11-07T00:00:00.000Z","contract_address":[{"contract_address":"0x4c769928971548eb71a3392eaf66bedc8bef4b80","platform":{"name":"BNB Smart Chain (BEP20)","coin":{"id":"1839","name":"BNB","symbol":"BNB","slug":"bnb"}}}],"self_reported_circulating_supply":274220519302082,"self_reported_tags":null,"self_reported_market_cap":260654.56496111778}}}'


# Convert string to Python dict
test_dict = json.loads(info_symbol)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print('Method 1:')
data = test_dict['data']['BITCOIN']
print(data['id'])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print()
print('Method 2:')
for key, value in test_dict['data']['BITCOIN'].items():
    if key=='id': #id, name, symbol
      print(value)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print()
print('Method 3: ')
print(test_dict['data']['BITCOIN']['id'] )


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# doesnt work
'''
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")
with open('jsonParse2.txt') as f:
    json_data = json.load(f)
'''


#test = "{'status': {'timestamp': '2023-01-22T23:18:38.233Z', 'error_code': 0, 'error_message': None, 'elapsed': 15, 'credit_count': 1, 'notice': None}, 'data': {'BTC': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'category': 'coin', 'description': 'Bitcoin (BTC) is a cryptocurrency . Users are able to generate BTC through the process of mining. Bitcoin has a current supply of 19,269,650. The last known price of Bitcoin is 22,725.84901486 USD and is down -0.92 over the last 24 hours. It is currently trading on 9942 active market(s) with $25,251,941,993.68 traded over the last 24 hours. More information can be found at https://bitcoin.org/.', 'slug': 'bitcoin', 'logo': 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png', 'subreddit': 'bitcoin', 'notice': '', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 'tag-names': ['Mineable', 'PoW', 'SHA-256', 'Store Of Value', 'State Channel', 'Coinbase Ventures Portfolio', 'Three Arrows Capital Portfolio', 'Polychain Capital Portfolio', 'Binance Labs Portfolio', 'Blockchain Capital Portfolio', 'BoostVC Portfolio', 'CMS Holdings Portfolio', 'DCG Portfolio', 'DragonFly Capital Portfolio', 'Electric Capital Portfolio', 'Fabric Ventures Portfolio', 'Framework Ventures Portfolio', 'Galaxy Digital Portfolio', 'Huobi Capital Portfolio', 'Alameda Research Portfolio', 'a16z Portfolio', '1Confirmation Portfolio', 'Winklevoss Capital Portfolio', 'USV Portfolio', 'Placeholder Ventures Portfolio', 'Pantera Capital Portfolio', 'Multicoin Capital Portfolio', 'Paradigm Portfolio'], 'tag-groups': ['OTHERS', 'ALGORITHM', 'ALGORITHM', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY', 'CATEGORY'], 'urls': {'website': ['https://bitcoin.org/'], 'twitter': [], 'message_board': ['https://bitcointalk.org'], 'chat': [], 'facebook': [], 'explorer': ['https://blockchain.coinmarketcap.com/chain/bitcoin', 'https://blockchain.info/', 'https://live.blockcypher.com/btc/', 'https://blockchair.com/bitcoin', 'https://explorer.viabtc.com/btc'], 'reddit': ['https://reddit.com/r/bitcoin'], 'technical_doc': ['https://bitcoin.org/bitcoin.pdf'], 'source_code': ['https://github.com/bitcoin/bitcoin'], 'announcement': []}, 'platform': None, 'date_added': '2013-04-28T00:00:00.000Z', 'twitter_username': '', 'is_hidden': 0, 'date_launched': None, 'contract_address': [], 'self_reported_circulating_supply': None, 'self_reported_tags': None, 'self_reported_market_cap': None}}}"
#new_dict = json5.loads(test)



#test = '{"status":{"timestamp":"2023-01-21T20:35:53.822Z","error_code":0,"error_message":null,"elapsed":15,"credit_count":1,"notice":null},"data":{"BTC":{"id":1,"name":"Bitcoin","symbol":"BTC","category":"coin","description":"Bitcoin (BTC) is a cryptocurrency . Users are able to generate BTC through the process of mining. Bitcoin has a current supply of 19,268,700. The last known price of Bitcoin is 23,184.29358498 USD and is up 6.11 over the last 24 hours. It is currently trading on 9942 active market(s) with $35,679,998,436.08 traded over the last 24 hours. More information can be found at https://bitcoin.org/.","slug":"bitcoin","logo":"https://s2.coinmarketcap.com/static/img/coins/64x64/1.png","subreddit":"bitcoin","notice":"","tags":["mineable","pow","sha-256","store-of-value","state-channel","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","galaxy-digital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio"],"tag-names":["Mineable","PoW","SHA-256","Store Of Value","State Channel","Coinbase Ventures Portfolio","Three Arrows Capital Portfolio","Polychain Capital Portfolio","Binance Labs Portfolio","Blockchain Capital Portfolio","BoostVC Portfolio","CMS Holdings Portfolio","DCG Portfolio","DragonFly Capital Portfolio","Electric Capital Portfolio","Fabric Ventures Portfolio","Framework Ventures Portfolio","Galaxy Digital Portfolio","Huobi Capital Portfolio","Alameda Research Portfolio","a16z Portfolio","1Confirmation Portfolio","Winklevoss Capital Portfolio","USV Portfolio","Placeholder Ventures Portfolio","Pantera Capital Portfolio","Multicoin Capital Portfolio","Paradigm Portfolio"],"tag-groups":["OTHERS","ALGORITHM","ALGORITHM","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY","CATEGORY"],"urls":{"website":["https://bitcoin.org/"],"twitter":[],"message_board":["https://bitcointalk.org"],"chat":[],"facebook":[],"explorer":["https://blockchain.coinmarketcap.com/chain/bitcoin","https://blockchain.info/","https://live.blockcypher.com/btc/","https://blockchair.com/bitcoin","https://explorer.viabtc.com/btc"],"reddit":["https://reddit.com/r/bitcoin"],"technical_doc":["https://bitcoin.org/bitcoin.pdf"],"source_code":["https://github.com/bitcoin/bitcoin"],"announcement":[]},"platform":null,"date_added":"2013-04-28T00:00:00.000Z","twitter_username":"","is_hidden":0,"date_launched":null,"contract_address":[],"self_reported_circulating_supply":null,"self_reported_tags":null,"self_reported_market_cap":null}}}'
#new_dict = json.loads(test)


'''
os.chdir("/Users/john/Desktop/GoogleDrive/ATBS/WebScraping/jsonParse")
with open('TEST.json') as f:
    json_data = json.load(f)
'''








