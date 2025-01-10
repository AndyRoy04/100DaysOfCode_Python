import requests
import os
from twilio.rest import Client

account_sid = 'YOUR TWILIO ACCOUNT SID'
auth_token = 'TWILIO AUTHENTICATION TOKEN'

API_KEY = 'YOUR API KEY FROM OPEN WEATHER' 
LAT = 39.0092017
LONG = -76.7682662

paramemters = {
    'lat':LAT,
    'lon': LONG,
    'appid': API_KEY,
    'cnt': 4  # Number of days forecast
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=paramemters)
response.raise_for_status()

weather_data = response.json()
list_length = len(weather_data['list'])
will_rain = False
for i in range(list_length):
    weather_id = weather_data['list'][i]['weather'][0]['id']
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+YOUR TWILIO NUMBER',
    body="It's going to rain today. Remember to take an umbrella ☔ with you.",
    to='whatsapp:+YOUR VERIFIED WHATSAPP NUMBER'
    )
    print(message.status)

