import json

# 1 JSON string in list, works
info_1_response = ['{"status": {"timestamp": "2023-01-25T22:59:58.760Z", "error_code": 0, "error_message": null, "elapsed": 16, "credit_count": 1, "notice": null}, "data": {"BTC": {"id": 1, "name": "Bitcoin", "symbol": "BTC"}}}']

for response in info_1_response:
    info_1_dict = json.loads(response)
    #print(info_1_dict) #works
    data = info_1_dict['data']['BTC']
    #print(f"only id = {data['id']}")
        #OUTPUT: only id = 1



info_2_response = ['{"status": {"timestamp": "2023-01-25T22:59:58.760Z", "error_code": 0, "error_message": null, "elapsed": 16, "credit_count": 1, "notice": null}, "data": {"BTC": {"id": 1, "name": "Bitcoin", "symbol": "BTC"}}}', '{"status": {"timestamp": "2023-01-25T22:59:59.087Z", "error_code": 0, "error_message": null, "elapsed": 16, "credit_count": 1, "notice": null}, "data": {"ETH": {"id": 1027, "name": "Ethereum", "symbol": "ETH"}}}']
for response in info_2_response:
    info_2_dict = json.loads(response)
    #print(info_2_dict) #works

    #Best way:
    for key, value in info_2_dict['data'].items():
        print(key, value['id'])


    #Alternatives:
    #print(info_2_dict['data']) #works
    #data = info_2_dict['data']['BTC']
    #print(f"only id = {data['id']}")
        #{'BTC': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC'}}
        #{'ETH': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH'}}
    #print(list(info_2_dict))
        #['status', 'data']
        #['status', 'data']  
    #print(list(info_2_dict['data'].values())[0]['id'])

#method 2 - works but I dont really like it
# for response in map(json.loads, info_2_response):
#     [(coin, data), *_] = response['data'].items()
#     print(coin, data['id'])

    

