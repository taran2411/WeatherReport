import requests
from datetime import datetime

api_key = 'bbaa89b506b1806e896f9f3bc0099779'
location =input("Enter the city name:")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link= requests.get(complete_api_link)
api_data=api_link.json()


temp_city =((api_data['main']['temp']) -273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime("%d  %b  %y | %I %M %S %p")
fileW= open('Weather Report.txt', 'w')


print("------------------------------------------------",file=fileW)
print("Weather Report for - {} || {}".format(location.upper(),date_time),file=fileW)
print("------------------------------------------------",file=fileW)

print("Current Temperature is: {:.2f} deg C".format(temp_city),file=fileW)
print("Current weather desc  :",weather_desc,file=fileW)
print("current Humidity      :",hmdt, '%',file=fileW)
print("current wind speed    :",wind_spd,'kmph',file=fileW)


fileW.close()
