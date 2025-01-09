import requests
import datetime as dt
import smtplib

MY_MAIL = 'codingjourney25@gmail.com'
MY_PASSWORD = 'xneamnxivfjkunsk'   # get this secure one time password for your app from the app passwords in google

LAT = 39.0092017
LONG = -76.7682662

# Function to check if latitude and Longitude are within range
def check_location():
    # --------------- ISS longitude and latitude Possition ---------------- #
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    
    # Check if ISS is within 5 degress of the user's location
    if (LAT-5 <= latitude <= LAT+5) and (LONG-5 <= longitude <= LONG+5):
        return True

def check_time():
    # Getting parameters to add to Sunrise and sunset json formats
    parameters = {
        "lat": LAT,
        "lng": LONG,
        'formatted': 0
    }

    # --------------- Sunrise and Sunset Hours ---------------- #
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    # --------------- Current Hour ---------------- #
    current_time = dt.datetime.now()
    current_hour = current_time.hour
    
    if current_hour >= (sunset - 6) or current_hour <= (sunrise - 6):   # -6 for converting from UTC to New york time
        return True

# --------------- Check if current location is within ISS's range ---------------- #
if check_location() and check_time():

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()   # start TLS connection which helps secure connection with our email server
        connection.login(user=MY_MAIL, password=MY_PASSWORD)   # specify your email address and password
        connection.sendmail(
            from_addr=MY_MAIL, 
            to_addrs='djeutio1234@gmail.com', # Change to the sender address
            msg='Subject:VIEW ISS\n\nISS is visible in your location'
            )   # Helps perform mail transaction between sender and receiver
