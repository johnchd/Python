import requests
import json

#change the "perPage" value here - I used 5 for poc. Change it to 50 or 100 for say.
url = 'https://cards.alarmsports.com/api/datatables/table-contents/97e86095-c34a-4b0e-a18e-3ea2704e583b/ajax?page=1&perPage=50&search=&sort=id&direction=1&col_filter_data=%7B%7D&data_filter_data=%7B%222%22:3,%224%22:84,%225%22:18%7D&injected_filter_data=%7B%7D'
response = requests.get(url)

jsonResponse = response.text
# print(type(jsonResponse)) #str

jsonParse = json.loads(jsonResponse)
# print(type(jsonParse))
# print(jsonParse)

# for player in jsonParse["items"]:
#     key_2_formatted = player.get("2", {}).get("formatted")
#     if key_2_formatted is not None:
#         print(key_2_formatted)

for player in jsonParse["items"]:
    # print(type(player))
    print(player["2"]["formatted"])
    print(player["4"])
    print("projection: " + player["6"])
    # print(player["7"]["unformatted"]["over"])
    # overUnder_data = player["7"]["unformatted"]["over"]
    # total_value = overUnder_data["metadata"]["total"]
    # print("Over/under: " + total_value)


    over_data = player["7"]["unformatted"]["over"]
    under_data = player["7"]["unformatted"]["under"]
    
    over_name = over_data.get("name")
    over_us_total = over_data.get("us_total")
    
    under_name = under_data.get("name")
    under_us_total = under_data.get("us_total")
    
    print(f"Over Odds: {over_us_total}")
    print(f"Under Odds: {under_us_total}")
    print("\n")






