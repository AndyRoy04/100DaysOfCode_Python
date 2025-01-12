import requests
import datetime as dt
import os

os.environ["API_ID"] = 'API ID FROM NUTRITIONIX'
os.environ["API_KEY"] = 'API KEY FROM NUTRITIONIX'
os.environ["SHEETY_USERNAME"] = 'FROM SHEETY URL'
os.environ["AUTHORIZATION_KEY"] = "FROM SHEETY AUTHENTICATOIN"

today_date = dt.datetime.now().strftime('%m/%d/%Y')
today_time = dt.datetime.now().strftime('%X')

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_URL = f'https://api.sheety.co/{os.environ["SHEETY_USERNAME"]}/personalWorkouts/workouts'

GENDER = 'male'
WEIGHT_KG = '90'
HEIGHT_CM = '1.91'
AGE = '21'

activity = input('What exercises did you do? : ')

headers = {
    'x-app-key': os.environ["API_KEY"],
    'x-app-Id': os.environ["API_ID"],
    'Content-Type': 'application/json',
}

sheety_header = {
    "Authorization": AUTHORIZATION_KEY
}

parameters = {
    'query': activity,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Retrieving all necessary data for our DataSheet from Nutritionix
response = requests.post(API_ENDPOINT, json=parameters, headers=headers)
data = response.json()

for content in data['exercises']:
    duration_min = content['duration_min']
    calories = content['nf_calories']
    exercise_name = content['name'].title()

    workout_data = {
        'workout': {
            "date": today_date,
            "time": today_time,
            "exercise": exercise_name,
            "duration": duration_min,
            "calories": calories,
        },
    }
    sheety_response = requests.post(
        url=SHEETY_URL, json=workout_data, headers=sheety_header)
print(sheety_response.status_code)
