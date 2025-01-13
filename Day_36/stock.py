import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = 'YOUR TWILIO ACCOUNT SID'     #replace
auth_token = 'TWILIO AUTHENTICATION TOKEN'      #replace

# STOCK URL and APIG
STOCK_URL = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'ALPHADVANTAGE API KEY'   #replace  

# STOCK NEWS URL and API
NEWS_URL = 'https://newsapi.org/v2/everything'
NEWS_URL_API = 'NEWS API API KEY'       #replace

# -------------------- FUNCTION TO CALCULATE PERCANTAGE DIFFERENCE ------------------------ #
def percentage_difference(old_price, new_price):
    """Calculates the percentage difference between two numbers."""
    difference = abs(new_price - old_price)
    percentage = (difference / old_price) * 100
    if new_price < old_price:
        return round((percentage * -1), 2)
    return round((percentage), 2)

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
news_parameters = {
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_URL_API
}

## Extracting stock price from https://www.alphavantage.co
stock_reponse = requests.get(url=STOCK_URL, params=parameters)
stock_reponse.raise_for_status()
stock_data = stock_reponse.json()
try:
    daily_price_dict = stock_data['Time Series (Daily)']
except KeyError:
    print(f"No data available for {STOCK} at the moment. Try again later")
else:
    price_data = list(daily_price_dict.values())[:2]   # Getting hold of the values from the previous daily prices
    today_open_price = float(price_data[0]['1. open'])
    yesterday_open_price = float(price_data[1]['1. open'])

    price_difference = percentage_difference(yesterday_open_price, today_open_price)

    if price_difference <= -5 or price_difference >= 5:
        if price_difference <= -5:
            price_difference = f'{STOCK}:  🔴 {price_difference}%'
        else:
            price_difference = f'{STOCK}:  🟢 {price_difference}%'

        ## Extracting stock news from https://newsapi.org
        news_response = requests.get(url='https://newsapi.org/v2/everything', params=news_parameters)
        news_response.raise_for_status()
        news_data = news_response.json()
        try:
            today_articles = news_data['articles'][:3]
        except IndexError:
            print(f'No articles found for {COMPANY_NAME} at the moment. Please try again later')
        else:
            news_formated = [f"{price_difference}\nHeadline: {item['title']}\n\nBrief: {item['description']}" for item in today_articles]

            client = Client(account_sid, auth_token)
            for article in news_formated:
                message = client.messages.create(
                from_='whatsapp:TWILIO PHONE NUMBER',       #replcae
                body=article,
                to='whatsapp:+VERIFIED WHATSAPP PHONE NUMBER'     #replcae  
                )
            print(message.status)
