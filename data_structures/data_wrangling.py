import json
from urllib.request import urlopen

people_String='''
{
  "people": [
{
    "name": "Jane Doe",
    "phone": "66474-48784",
    "emails": null,
    "has_license": true
},{
    "name": "John smith",
    "phone": "615-555-7164",
    "emails": ["johnsmith@bogusemail.com", "john.smith@workplace.com"],
    "has_license": false
}
  ]
}
'''

data = json.loads(people_String)

print(type(data['people']))

for person in data['people']:
    print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


# with open('people.json', 'w') as f:
#     json.dump(data, f, indent=2)

with open('people.json', 'r') as f:
    data = json.load(f)

print(data)

with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    source = response.read()

print(source)