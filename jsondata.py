import json

with open("r1.json") as file:
    data = json.load(file)

print(data['router']['interfaces'][0]['ip'])
