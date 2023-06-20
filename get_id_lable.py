import json, re

file_path = "call.json"

with open(file_path, 'r') as file:
    json_data = file.read()

data = json.loads(json_data)

label_id_map = {}

for item in data:
    label = item['label']
    label_id_map[item['id']] = label

print(label_id_map)

