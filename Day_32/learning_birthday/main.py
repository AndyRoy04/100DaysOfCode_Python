import smtplib

my_email = 'codingjourney25@gmail.com'
my_password = 'xneamnxivfjkunsk'   # get this secure one time password for your app from the app passwords in google

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()   # start TLS connection which helps secure connection with our email server
    connection.login(user=my_email, password=my_password)   # specify your email address and password
    connection.sendmail(
        from_addr=my_email, 
        to_addrs='codingjourney25@gmail.com', # Change to the sender address
        msg='Subject:For Ma Men Dem\n\nHey Nigga, this is for you')   # Helps perform mail transaction between sender and receiver


# import datetime as dt

# current_date_time = dt.datetime.now()
# year = current_date_time.year
# week_day = current_date_time.weekday()

# print(week_day)
# # print(year)

# date_of_birth = dt.datetime(year=2004, month=4, day=10)
# print(date_of_birth)
