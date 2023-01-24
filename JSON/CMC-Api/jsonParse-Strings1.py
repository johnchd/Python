import json
import requests
from requests.auth import HTTPBasicAuth
import urllib.request
 
#Part 1 - Retrive/convert JSON string (normally this would be a file)
#Part 2 - Parse that JSON string, collect slugs, and insert into list
#Part 3 - Insert slugs from list into URL / print URLs
#Part 4 - get JSON response of each SLUG


#Part 1 - JSON string
print()
print('Part 1 --- JSON output that is not shown. - Only using BTC for PoC')
test = '{"status":{"timestamp":"2023-01-16T20:32:58.871Z","error_code":0,"error_message":null,"elapsed":23,"credit_count":1,"notice":null,"total_count":8865},"data":[{"id":1,"name":"Bitcoin","symbol":"BTC","slug":"bitcoin","num_market_pairs":9932,"date_added":"2013-04-28T00:00:00.000Z","tags":["mineable","pow","sha-256","store-of-value","state-channel","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","galaxy-digital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio"],"max_supply":21000000,"circulating_supply":19264237,"total_supply":19264237,"platform":null,"cmc_rank":1,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":21335.752537474465,"volume_24h":26059518298.700356,"volume_change_24h":31.6595,"percent_change_1h":0.19884237,"percent_change_24h":2.2015074,"percent_change_7d":23.66840934,"percent_change_30d":27.70574198,"percent_change_60d":28.08345886,"percent_change_90d":10.58380127,"market_cap":411016993455.25946,"market_cap_dominance":41.2685,"fully_diluted_market_cap":448050803286.96,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}}]}'
test_dict = json.loads(test)

#Part 2 - Slugs into list
nameList = []
#prints all names AND adds to list
print()
for name in test_dict['data']:
    #print(name['name']) #id, name, symbol, slug, etc
    nameList.append(name['slug'])
print('Part 2 --- List of slugs:\n' + str(nameList))

#Part 3 - Insert slugs from list into URL
print()
print('Part 3 --- Slugs appended to URL:')
for i in nameList:
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={}'.format(i)
    print(url)

#Part 4 - get JSON response of each SLUG
print()
print('Part 4 --- Parsing the response each SLUG ')
print(url)

#authenticate
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<api-key>',
}

req = requests.get(url, headers=headers)

#this gets the ALL the contents of a response
x = req.content
#print(x)

#create new file
newFile = open("btcInfo.txt", "a")
newFile.write(str(x))
