import smtplib
import datetime as dt
import pandas
import random

MY_MAIL = 'codingjourney25@gmail.com'
MY_PASSWORD = 'xneamnxivfjkunsk'
DATE = dt.datetime.now()
MONTH = DATE.month
DAY = DATE.day

# creating empty arrays in case of multiple same birthdays
names = []
emails = []
try:
    birthdays = pandas.read_csv('100DaysOfCode_Python/Day_32/birthday_code/birthdays.csv')
except FileNotFoundError:
    print('File not found')

# iterating through the dataframe to get the birthdays
for index, row in birthdays.iterrows():
    if row.month == MONTH and row.day == DAY:
        names.append(row['name'])
        emails.append(row.email)

# Creating the messages from the names
email_count = 0        
for someone in names:
    random_number = random.randint(1, 10)
    with open(f'100DaysOfCode_Python/Day_32/birthday_code/letter_templates/letter_{random_number}.txt') as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace('[NAME]', someone)
        
    # Sending the mails to different recipients
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        connection.sendmail(MY_MAIL, emails[email_count], msg=f'Subject: Birthday Wish\n\n{letter_content}')
        email_count += 1
