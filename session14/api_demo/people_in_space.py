import urllib.request
import json
import pprint

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as response:
    response_text = response.read().decode("utf-8")
    # print(response_text)
    # print(type(response_text))
    data = json.loads(response_text)
    # print(data)
    # print(type(data))
    pprint.pprint(data)

# Can you print number of people in the space?
# print(len(data))
# print(data.keys())
n = data['number']
print(n)


# Can you print all the names and their space stations?
people = data['people']  # this is a list of dicts
# print(type(people))
# print(type(people[0]))

for p in people:
    print(p['name'], p['craft'])

