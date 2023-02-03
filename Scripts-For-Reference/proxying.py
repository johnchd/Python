import requests

proxies = {

    'http' : 'http://127.0.0.1:8080'
}

response = requests.get("http://google.com", proxies=proxies)
print(response)