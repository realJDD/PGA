import json
import requests


r = requests.get('https://statdata.pgatour.com/players/25198/2019stat.json')
json_data = json.loads(r.text)

statID = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][1]['statID']
name = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][1]['name']
value = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][1]['value']
rank = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][1]['rank']
add_value = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][0]['additionals'][0]['value']
add_title = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][0]['additionals'][0]['title']
add_value_1 = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][0]['additionals'][1]['value']
add_title_1 = json_data['plrs'][0]['years'][0]['tours'][0]['statCats'][0]['stats'][0]['additionals'][1]['title']


print(f"statID: {statID}")
print(f"name: {name}")
print(f"value: {value}")
print(f"rank: {rank}")
print(f"add_value: {add_value}")
print(f"add_title: {add_title}")
print(f"add_value_1: {add_value_1}")
print(f"add_title_1: {add_title_1}")
