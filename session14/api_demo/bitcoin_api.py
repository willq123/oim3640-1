import urllib.request
import json
import pprint

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

with urllib.request.urlopen(url) as response:
    response_text = response.read().decode("utf-8")
    # print(response_text)
    # print(type(response_text))
    data = json.loads(response_text)
    # print(data)
    # print(type(data))
    # pprint.pprint(data)

# price in USD

# pprint.pprint(data['bpi'])
price_in_usd = data['bpi']['USD']['rate_float']
print(price_in_usd)


