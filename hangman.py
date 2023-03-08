import json


f = open('words.json')
data = json.load(f)

print(data)