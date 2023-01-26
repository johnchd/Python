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






