
import requests
import json
import config
from datetime import date,timedelta
city = input('enter city:')
api_link = 'http://api.weatherapi.com/v1/forecast.json?key='+config.API_KEY+'&q='+city+'&days=10&aqi=yes&alerts=yes'

try:
    api_request = requests.get(api_link)
    x = json.loads(api_request.content)
    # current weather conditions

    print("current weather conditions:")
    print("name:"+str(x['location']['name']))
    print("time:"+str(x['location']['localtime']))
    print("temperature in celsius::" + str(x['current']['temp_c']))
    print("temperature in fahrenheit:" + str(x['current']['temp_f']))
    print("current condition:" + str(x['current']['condition']['text']))

    print("wind speed in mph:" + str(x['current']["wind_mph"]))
    print("wind speed in kph:" + str(x['current']["wind_kph"]))
    print("humidity:"+str(x['current']["humidity"]))
    print('uv:'+str(x['current']['uv']))
    print('air quality:')
    print('CO:'+str(x['current']['air_quality']['co']))
    print('NO2:' + str(x['current']['air_quality']['no2']))
    print('O3:' + str(x['current']['air_quality']['o3']))
    print('SO2:' + str(x['current']['air_quality']['so2']))

    print('daily forecast:')
    for i in range(0,10):
        print('date:'+str(x['forecast']['forecastday'][i]['date']))
        print('maximum temperature in celsius:'+str(x['forecast']['forecastday'][i]['day']['maxtemp_c']))
        print('maximum temperature in fahrenheit:' + str(x['forecast']['forecastday'][i]['day']['maxtemp_f']))
        print('minimum temperature in celsius:' + str(x['forecast']['forecastday'][i]['day']['mintemp_c']))
        print('minimum temperature in fahrenheit:' + str(x['forecast']['forecastday'][i]['day']['mintemp_f']))
        print('average temperature in celsius:' + str(x['forecast']['forecastday'][i]['day']['avgtemp_c']))
        print('average temperature in fahrenheit:' + str(x['forecast']['forecastday'][i]['day']['avgtemp_f']))
        print('maximum wind in mph:' + str(x['forecast']['forecastday'][i]['day']['maxwind_mph']))
        print('maximum wind in kph:' + str(x['forecast']['forecastday'][i]['day']['maxwind_kph']))
        print('total precipitation in mm:' + str(x['forecast']['forecastday'][i]['day']['totalprecip_mm']))


        print('sunset:' + str(x['forecast']['forecastday'][i]['astro']['sunset']))
        print('average humidity:' + str(x['forecast']['forecastday'][i]['day']['avghumidity']))
        print('moonrise:' + str(x['forecast']['forecastday'][i]['astro']['moonrise']))
        print('moonset:' + str(x['forecast']['forecastday'][i]['astro']['moonset']))
        print('moon phase:' + str(x['forecast']['forecastday'][i]['astro']['moon_phase']))
        print('sunrise:' + str(x['forecast']['forecastday'][i]['astro']['sunrise']))
        print("hourly forecast:")
        for j in range(0,24):
            print("time:" + str(x['forecast']['forecastday'][i]['hour'][j]['time']))
            print("temperature in celsius:"+str(x['forecast']['forecastday'][i]['hour'][j]['temp_c']))
            print("wind speed in mph:"+str(x['forecast']['forecastday'][i]['hour'][j]['wind_mph']))
            print("precipitation in mm:" + str(x['forecast']['forecastday'][i]['hour'][j]['precip_mm']))
            print("humidity:" + str(x['forecast']['forecastday'][i]['hour'][j]['humidity']))





except Exception as e:
    x = "Error"
    print("error")





