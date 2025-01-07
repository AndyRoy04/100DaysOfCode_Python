import smtplib
import datetime as dt
import random

DAYS= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# getting the day of the week from the datetime class
year_date = dt.datetime.now()
week_day = year_date.weekday()

# getting a random quote from a txt file
try:
    with open('100DaysOfCode_Python/Day_32/Birthday_wisher/quotes.txt') as quotes:
        # quotes_list = [quote.strip() for quote in quotes.readlines()]
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)
except FileNotFoundError:
    print('Quotes file not found.')        

my_email = 'codingjourney25@gmail.com'
my_password = 'xneamnxivfjkunsk'   # get this secure one time password for your app from the app passwords in google

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()   # start TLS connection which helps secure connection with our email server
    connection.login(user=my_email, password=my_password)   # specify your email address and password
    connection.sendmail(
        from_addr=my_email, 
        to_addrs='andersonroy.lead@yahoo.com', 
        msg=f'Subject:{DAYS[week_day]} Motivation\n\n{random_quote}')