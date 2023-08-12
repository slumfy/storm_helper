import json
from unicodedata import name

# Opening JSON file
f = open('cards_base.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data:
	json_str = json.dumps(data[i])
	print(json_str)

# Closing file
f.close()