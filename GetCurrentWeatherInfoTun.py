import json
import requests
from Secret import OpenWeatherApi_Key

# Old requests for current weather in tunisia
'''
print("\nGettting Data As Json...")

r = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=2464470&units=imperial&APPID='+ OpenWeatherApi_Key)
with open('TunisWeatherData.json', 'w+') as f:
    f.write(r.text)


with open('TunisWeatherData.json', 'r+', encoding="UTF-8") as f:
    tunis_data = json.load(f)
print(tunis_data)

print("\nParsing Data....")


print("\nTempretaure in Tunis is :{} fahrenheit".format(tunis_data['list'][0]['main']["temp"]))
'''