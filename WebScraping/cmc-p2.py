#!/usr/bin/python3

import re


name = re.compile(r'''(
    \"name\":"\w+" 
    )''', re.VERBOSE)

price = re.compile(r'''(
    \"price\":\d+\W\d{5}
    )''', re.VERBOSE)

x = name.findall('''
b'{"status":{"timestamp":"2023-01-16T20:32:58.871Z","error_code":0,"error_message":null,"elapsed":23,"credit_count":1,"notice":null,"total_count":8865},"data":[{"id":1,"name":"Bitcoin","symbol":"BTC","slug":"bitcoin","num_market_pairs":9932,"date_added":"2013-04-28T00:00:00.000Z","tags":["mineable","pow","sha-256","store-of-value","state-channel","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","galaxy-digital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio"],"max_supply":21000000,"circulating_supply":19264237,"total_supply":19264237,"platform":null,"cmc_rank":1,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":21335.752537474465,"volume_24h":26059518298.700356,"volume_change_24h":31.6595,"percent_change_1h":0.19884237,"percent_change_24h":2.2015074,"percent_change_7d":23.66840934,"percent_change_30d":27.70574198,"percent_change_60d":28.08345886,"percent_change_90d":10.58380127,"market_cap":411016993455.25946,"market_cap_dominance":41.2685,"fully_diluted_market_cap":448050803286.96,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","num_market_pairs":6361,"date_added":"2015-08-07T00:00:00.000Z","tags":["pos","smart-contracts","ethereum-ecosystem","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","hashkey-capital-portfolio","kenetic-capital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio","injective-ecosystem"],"max_supply":null,"circulating_supply":122373866.2178,"total_supply":122373866.2178,"platform":null,"cmc_rank":2,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1592.061180053041,"volume_24h":8206826690.369308,"volume_change_24h":16.8774,"percent_change_1h":0.37534723,"percent_change_24h":2.73183238,"percent_change_7d":20.11564633,"percent_change_30d":35.16895649,"percent_change_60d":32.18738789,"percent_change_90d":21.88397684,"market_cap":194826681858.36365,"market_cap_dominance":19.551,"fully_diluted_market_cap":194826681858.36,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":825,"name":"Tether","symbol":"USDT","slug":"tether","num_market_pairs":46161,"date_added":"2015-02-25T00:00:00.000Z","tags":["payments","stablecoin","asset-backed-stablecoin","avalanche-ecosystem","solana-ecosystem","arbitrum-ecosytem","moonriver-ecosystem","injective-ecosystem","bnb-chain","usd-stablecoin"],"max_supply":null,"circulating_supply":66355388816.4582,"total_supply":73141766321.23428,"platform":{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0xdac17f958d2ee523a2206206994597c13d831ec7"},"cmc_rank":3,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.0001516528050478,"volume_24h":35526476515.202324,"volume_change_24h":16.2772,"percent_change_1h":-0.00071467,"percent_change_24h":-0.02091767,"percent_change_7d":0.01669852,"percent_change_30d":0.00106022,"percent_change_60d":0.072552,"percent_change_90d":0.00382126,"market_cap":66365451797.30225,"market_cap_dominance":6.6578,"fully_diluted_market_cap":73152858475.26,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":1839,"name":"BNB","symbol":"BNB","slug":"bnb","num_market_pairs":1169,"date_added":"2017-07-25T00:00:00.000Z","tags":["marketplace","centralized-exchange","payments","smart-contracts","alameda-research-portfolio","multicoin-capital-portfolio","bnb-chain"],"max_supply":200000000,"circulating_supply":159961821.65524235,"total_supply":159979963.59042934,"platform":null,"cmc_rank":4,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":300.92659196167057,"volume_24h":587766105.994197,"volume_change_24h":2.3053,"percent_change_1h":0.21224279,"percent_change_24h":-0.05395721,"percent_change_7d":9.81870494,"percent_change_30d":27.75574176,"percent_change_60d":12.06392798,"percent_change_90d":10.25898209,"market_cap":48136765834.692635,"market_cap_dominance":4.8291,"fully_diluted_market_cap":60185318392.33,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":3408,"name":"USD Coin","symbol":"USDC","slug":"usd-coin","num_market_pairs":9555,"date_added":"2018-10-08T00:00:00.000Z","tags":["medium-of-exchange","stablecoin","asset-backed-stablecoin","fantom-ecosystem","arbitrum-ecosytem","moonriver-ecosystem","bnb-chain","usd-stablecoin"],"max_supply":null,"circulating_supply":43850655812.15361,"total_supply":43850655812.15361,"platform":{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"},"cmc_rank":5,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.0000103086994132,"volume_24h":2903905067.6269064,"volume_change_24h":6.7342,"percent_change_1h":-0.00449677,"percent_change_24h":0.00018074,"percent_change_7d":0.01445585,"percent_change_30d":0.01180863,"percent_change_60d":-0.03380137,"percent_change_90d":-0.00900428,"market_cap":43851107855.38345,"market_cap_dominance":4.4005,"fully_diluted_market_cap":43851107855.38,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":52,"name":"XRP","symbol":"XRP","slug":"xrp","num_market_pairs":875,"date_added":"2013-08-04T00:00:00.000Z","tags":["medium-of-exchange","enterprise-solutions","arrington-xrp-capital-portfolio","galaxy-digital-portfolio","a16z-portfolio","pantera-capital-portfolio"],"max_supply":100000000000,"circulating_supply":50713323547,"total_supply":99989156648,"platform":null,"cmc_rank":6,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":0.39309768377556864,"volume_24h":1425948401.253074,"volume_change_24h":75.8837,"percent_change_1h":0.38494329,"percent_change_24h":2.07680067,"percent_change_7d":11.55933537,"percent_change_30d":12.14702639,"percent_change_60d":2.67564745,"percent_change_90d":-15.71080112,"market_cap":19935290022.886703,"market_cap_dominance":2.0005,"fully_diluted_market_cap":39309768377.56,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":4687,"name":"Binance USD","symbol":"BUSD","slug":"binance-usd","num_market_pairs":6027,"date_added":"2019-09-20T00:00:00.000Z","tags":["stablecoin","asset-backed-stablecoin","binance-chain","harmony-ecosystem","moonriver-ecosystem","usd-stablecoin"],"max_supply":null,"circulating_supply":16242596010.614058,"total_supply":16242596010.614058,"platform":{"id":1839,"name":"BNB","symbol":"BNB","slug":"bnb","token_address":"BUSD-BD1"},"cmc_rank":7,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.00042273073428,"volume_24h":8889893821.29438,"volume_change_24h":17.889,"percent_change_1h":0.00419892,"percent_change_24h":0.01244649,"percent_change_7d":0.01988907,"percent_change_30d":0.08981553,"percent_change_60d":0.02266163,"percent_change_90d":-0.03185352,"market_cap":16249462255.152237,"market_cap_dominance":1.6301,"fully_diluted_market_cap":16249462255.15,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":2010,"name":"Cardano","symbol":"ADA","slug":"cardano","num_market_pairs":636,"date_added":"2017-10-01T00:00:00.000Z","tags":["dpos","pos","platform","research","smart-contracts","staking","cardano-ecosystem","cardano"],"max_supply":45000000000,"circulating_supply":34518349157.412,"total_supply":35303937971.934,"platform":null,"cmc_rank":8,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":0.3540135346593838,"volume_24h":395301876.9159602,"volume_change_24h":9.2342,"percent_change_1h":0.02965646,"percent_change_24h":1.50945402,"percent_change_7d":12.63033981,"percent_change_30d":34.40177242,"percent_change_60d":8.70869629,"percent_change_90d":-2.67021308,"market_cap":12219962795.822186,"market_cap_dominance":1.2259,"fully_diluted_market_cap":15930609059.67,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":74,"name":"Dogecoin","symbol":"DOGE","slug":"dogecoin","num_market_pairs":634,"date_added":"2013-12-15T00:00:00.000Z","tags":["mineable","pow","scrypt","medium-of-exchange","memes","payments","doggone-doggerel","bnb-chain"],"max_supply":null,"circulating_supply":132670764299.89409,"total_supply":132670764299.89409,"platform":null,"cmc_rank":9,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":0.0847701274822128,"volume_24h":550751314.4759672,"volume_change_24h":10.9629,"percent_change_1h":0.06247424,"percent_change_24h":-0.46835616,"percent_change_7d":11.25210702,"percent_change_30d":9.15874677,"percent_change_60d":0.23561676,"percent_change_90d":42.96333724,"market_cap":11246517602.864628,"market_cap_dominance":1.1292,"fully_diluted_market_cap":11246517602.86,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":3890,"name":"Polygon","symbol":"MATIC","slug":"polygon","num_market_pairs":571,"date_added":"2019-04-28T00:00:00.000Z","tags":["platform","enterprise-solutions","scaling","state-channel","coinbase-ventures-portfolio","binance-launchpad","binance-labs-portfolio","polygon-ecosystem","moonriver-ecosystem","injective-ecosystem"],"max_supply":10000000000,"circulating_supply":8734317475.28493,"total_supply":10000000000,"platform":null,"cmc_rank":10,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.0141840977256735,"volume_24h":632197964.3922756,"volume_change_24h":47.8231,"percent_change_1h":0.24946219,"percent_change_24h":2.84858615,"percent_change_7d":20.15526692,"percent_change_30d":26.54985285,"percent_change_60d":15.71587934,"percent_change_90d":17.77656864,"market_cap":8858205887.921429,"market_cap_dominance":0.8887,"fully_diluted_market_cap":10141840977.26,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}}]}'
''')
y = price.findall('''
b'{"status":{"timestamp":"2023-01-16T20:32:58.871Z","error_code":0,"error_message":null,"elapsed":23,"credit_count":1,"notice":null,"total_count":8865},"data":[{"id":1,"name":"Bitcoin","symbol":"BTC","slug":"bitcoin","num_market_pairs":9932,"date_added":"2013-04-28T00:00:00.000Z","tags":["mineable","pow","sha-256","store-of-value","state-channel","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","galaxy-digital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio"],"max_supply":21000000,"circulating_supply":19264237,"total_supply":19264237,"platform":null,"cmc_rank":1,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":21335.752537474465,"volume_24h":26059518298.700356,"volume_change_24h":31.6595,"percent_change_1h":0.19884237,"percent_change_24h":2.2015074,"percent_change_7d":23.66840934,"percent_change_30d":27.70574198,"percent_change_60d":28.08345886,"percent_change_90d":10.58380127,"market_cap":411016993455.25946,"market_cap_dominance":41.2685,"fully_diluted_market_cap":448050803286.96,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","num_market_pairs":6361,"date_added":"2015-08-07T00:00:00.000Z","tags":["pos","smart-contracts","ethereum-ecosystem","coinbase-ventures-portfolio","three-arrows-capital-portfolio","polychain-capital-portfolio","binance-labs-portfolio","blockchain-capital-portfolio","boostvc-portfolio","cms-holdings-portfolio","dcg-portfolio","dragonfly-capital-portfolio","electric-capital-portfolio","fabric-ventures-portfolio","framework-ventures-portfolio","hashkey-capital-portfolio","kenetic-capital-portfolio","huobi-capital-portfolio","alameda-research-portfolio","a16z-portfolio","1confirmation-portfolio","winklevoss-capital-portfolio","usv-portfolio","placeholder-ventures-portfolio","pantera-capital-portfolio","multicoin-capital-portfolio","paradigm-portfolio","injective-ecosystem"],"max_supply":null,"circulating_supply":122373866.2178,"total_supply":122373866.2178,"platform":null,"cmc_rank":2,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1592.061180053041,"volume_24h":8206826690.369308,"volume_change_24h":16.8774,"percent_change_1h":0.37534723,"percent_change_24h":2.73183238,"percent_change_7d":20.11564633,"percent_change_30d":35.16895649,"percent_change_60d":32.18738789,"percent_change_90d":21.88397684,"market_cap":194826681858.36365,"market_cap_dominance":19.551,"fully_diluted_market_cap":194826681858.36,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":825,"name":"Tether","symbol":"USDT","slug":"tether","num_market_pairs":46161,"date_added":"2015-02-25T00:00:00.000Z","tags":["payments","stablecoin","asset-backed-stablecoin","avalanche-ecosystem","solana-ecosystem","arbitrum-ecosytem","moonriver-ecosystem","injective-ecosystem","bnb-chain","usd-stablecoin"],"max_supply":null,"circulating_supply":66355388816.4582,"total_supply":73141766321.23428,"platform":{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0xdac17f958d2ee523a2206206994597c13d831ec7"},"cmc_rank":3,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.0001516528050478,"volume_24h":35526476515.202324,"volume_change_24h":16.2772,"percent_change_1h":-0.00071467,"percent_change_24h":-0.02091767,"percent_change_7d":0.01669852,"percent_change_30d":0.00106022,"percent_change_60d":0.072552,"percent_change_90d":0.00382126,"market_cap":66365451797.30225,"market_cap_dominance":6.6578,"fully_diluted_market_cap":73152858475.26,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":1839,"name":"BNB","symbol":"BNB","slug":"bnb","num_market_pairs":1169,"date_added":"2017-07-25T00:00:00.000Z","tags":["marketplace","centralized-exchange","payments","smart-contracts","alameda-research-portfolio","multicoin-capital-portfolio","bnb-chain"],"max_supply":200000000,"circulating_supply":159961821.65524235,"total_supply":159979963.59042934,"platform":null,"cmc_rank":4,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":300.92659196167057,"volume_24h":587766105.994197,"volume_change_24h":2.3053,"percent_change_1h":0.21224279,"percent_change_24h":-0.05395721,"percent_change_7d":9.81870494,"percent_change_30d":27.75574176,"percent_change_60d":12.06392798,"percent_change_90d":10.25898209,"market_cap":48136765834.692635,"market_cap_dominance":4.8291,"fully_diluted_market_cap":60185318392.33,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":3408,"name":"USD Coin","symbol":"USDC","slug":"usd-coin","num_market_pairs":9555,"date_added":"2018-10-08T00:00:00.000Z","tags":["medium-of-exchange","stablecoin","asset-backed-stablecoin","fantom-ecosystem","arbitrum-ecosytem","moonriver-ecosystem","bnb-chain","usd-stablecoin"],"max_supply":null,"circulating_supply":43850655812.15361,"total_supply":43850655812.15361,"platform":{"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"},"cmc_rank":5,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.0000103086994132,"volume_24h":2903905067.6269064,"volume_change_24h":6.7342,"percent_change_1h":-0.00449677,"percent_change_24h":0.00018074,"percent_change_7d":0.01445585,"percent_change_30d":0.01180863,"percent_change_60d":-0.03380137,"percent_change_90d":-0.00900428,"market_cap":43851107855.38345,"market_cap_dominance":4.4005,"fully_diluted_market_cap":43851107855.38,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":52,"name":"XRP","symbol":"XRP","slug":"xrp","num_market_pairs":875,"date_added":"2013-08-04T00:00:00.000Z","tags":["medium-of-exchange","enterprise-solutions","arrington-xrp-capital-portfolio","galaxy-digital-portfolio","a16z-portfolio","pantera-capital-portfolio"],"max_supply":100000000000,"circulating_supply":50713323547,"total_supply":99989156648,"platform":null,"cmc_rank":6,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":0.39309768377556864,"volume_24h":1425948401.253074,"volume_change_24h":75.8837,"percent_change_1h":0.38494329,"percent_change_24h":2.07680067,"percent_change_7d":11.55933537,"percent_change_30d":12.14702639,"percent_change_60d":2.67564745,"percent_change_90d":-15.71080112,"market_cap":19935290022.886703,"market_cap_dominance":2.0005,"fully_diluted_market_cap":39309768377.56,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":4687,"name":"Binance USD","symbol":"BUSD","slug":"binance-usd","num_market_pairs":6027,"date_added":"2019-09-20T00:00:00.000Z","tags":["stablecoin","asset-backed-stablecoin","binance-chain","harmony-ecosystem","moonriver-ecosystem","usd-stablecoin"],"max_supply":null,"circulating_supply":16242596010.614058,"total_supply":16242596010.614058,"platform":{"id":1839,"name":"BNB","symbol":"BNB","slug":"bnb","token_address":"BUSD-BD1"},"cmc_rank":7,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.00042273073428,"volume_24h":8889893821.29438,"volume_change_24h":17.889,"percent_change_1h":0.00419892,"percent_change_24h":0.01244649,"percent_change_7d":0.01988907,"percent_change_30d":0.08981553,"percent_change_60d":0.02266163,"percent_change_90d":-0.03185352,"market_cap":16249462255.152237,"market_cap_dominance":1.6301,"fully_diluted_market_cap":16249462255.15,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":2010,"name":"Cardano","symbol":"ADA","slug":"cardano","num_market_pairs":636,"date_added":"2017-10-01T00:00:00.000Z","tags":["dpos","pos","platform","research","smart-contracts","staking","cardano-ecosystem","cardano"],"max_supply":45000000000,"circulating_supply":34518349157.412,"total_supply":35303937971.934,"platform":null,"cmc_rank":8,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":0.3540135346593838,"volume_24h":395301876.9159602,"volume_change_24h":9.2342,"percent_change_1h":0.02965646,"percent_change_24h":1.50945402,"percent_change_7d":12.63033981,"percent_change_30d":34.40177242,"percent_change_60d":8.70869629,"percent_change_90d":-2.67021308,"market_cap":12219962795.822186,"market_cap_dominance":1.2259,"fully_diluted_market_cap":15930609059.67,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":74,"name":"Dogecoin","symbol":"DOGE","slug":"dogecoin","num_market_pairs":634,"date_added":"2013-12-15T00:00:00.000Z","tags":["mineable","pow","scrypt","medium-of-exchange","memes","payments","doggone-doggerel","bnb-chain"],"max_supply":null,"circulating_supply":132670764299.89409,"total_supply":132670764299.89409,"platform":null,"cmc_rank":9,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":0.0847701274822128,"volume_24h":550751314.4759672,"volume_change_24h":10.9629,"percent_change_1h":0.06247424,"percent_change_24h":-0.46835616,"percent_change_7d":11.25210702,"percent_change_30d":9.15874677,"percent_change_60d":0.23561676,"percent_change_90d":42.96333724,"market_cap":11246517602.864628,"market_cap_dominance":1.1292,"fully_diluted_market_cap":11246517602.86,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}},{"id":3890,"name":"Polygon","symbol":"MATIC","slug":"polygon","num_market_pairs":571,"date_added":"2019-04-28T00:00:00.000Z","tags":["platform","enterprise-solutions","scaling","state-channel","coinbase-ventures-portfolio","binance-launchpad","binance-labs-portfolio","polygon-ecosystem","moonriver-ecosystem","injective-ecosystem"],"max_supply":10000000000,"circulating_supply":8734317475.28493,"total_supply":10000000000,"platform":null,"cmc_rank":10,"self_reported_circulating_supply":null,"self_reported_market_cap":null,"tvl_ratio":null,"last_updated":"2023-01-16T20:31:00.000Z","quote":{"USD":{"price":1.0141840977256735,"volume_24h":632197964.3922756,"volume_change_24h":47.8231,"percent_change_1h":0.24946219,"percent_change_24h":2.84858615,"percent_change_7d":20.15526692,"percent_change_30d":26.54985285,"percent_change_60d":15.71587934,"percent_change_90d":17.77656864,"market_cap":8858205887.921429,"market_cap_dominance":0.8887,"fully_diluted_market_cap":10141840977.26,"tvl":null,"last_updated":"2023-01-16T20:31:00.000Z"}}}]}'
''')

#prints btc and price
print(x[0],y[0])

#prints eth and price
#print(x[1],y[1])



#output is a little bit messed up but this is enoough for POC
print()
for name, price in zip(x, y):
    print(name + ' - ' + price)







   






     








