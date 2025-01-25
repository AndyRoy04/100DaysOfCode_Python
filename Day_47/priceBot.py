import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

TEST_MAIL = os.getenv('TEST_EMAIL')
MY_MAIL = os.getenv('ORIGINAL_EMAIL')
PASSWORD = os.getenv('MAIL_PASSWORD')
SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')
# ---------------------- ACCEPTED SERVER HEADERS ---------------------------#
AGENT = os.getenv('USER_AGENT')
FORMATS = os.getenv('FORMATS')
LANGUAGE = os.getenv('LANGUAGE')

# **** ASIDE ****
# You can use this to check your browser headers passed when you make a request on the internet
# url = https://httpbin.org/headers

# ------------------------ AMAZON PRODUCT URL ---------------------------#
ITEM_URL = 'https://www.amazon.com/Sony-PlayStation-Disc-Version-Renewed-3/dp/B09RTWS8PY/ref=sr_1_8?dib=eyJ2IjoiMSJ9.nRLN6tL2VMjei1uWpjwzT4qGvSslcjOS8uv3pS7IdKq5t5eKiPmR61HF3GldyY-ipjbBGiuF0xkV2lMrsNQDgNl3bcZDqgqkWBr0Z3cT4BnYwBPsntK42KwFcZB4IM7KPXGJfMfjRcEr-bLxoH2l3NMAesBCI-YJ31-OY819pa2u6RhumW_K3C-vgeWgNKjAGoHjJ1tGHOoVVIxyKeP5CL-9sVgZdz-eIGLcx6ZmLnQ.AiWn1cjQfN-74Eaysr4_WAP4vX00KWvWa1AwuZ6yRRc&dib_tag=se&keywords=ps5&qid=1737690460&sr=8-8'

# ------------------------ GETTING THE WEBSITE PAGE ------------------------#
headers = {
    'User-Agent': AGENT,
    'Accept': FORMATS,
    'Accept-Language': LANGUAGE,
}
response = requests.get(ITEM_URL, headers=headers)
source = response.text
soup = BeautifulSoup(source, 'html.parser')

# ------------------------ GETTING PRICE AND NAME OF PRODUCT ---------------#
price_tag = soup.find(class_='a-offscreen')
item_tag = soup.find(id='productTitle')
item_name = item_tag.getText().strip(' ')
price = float(price_tag.getText().split('$')[1])
# print(f'{item_name} is now at just ${price}')

# ----------------------- SENDING AN EMAIL AT A PARTICULAR PRICE ----------#
FIXED_PRICE = 450
if price < FIXED_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(TEST_MAIL, PASSWORD)
        subject = f'AMAZON PRICE ALERT'
        body = f'{item_name} is now at just ${price}'
        connection.sendmail(TEST_MAIL,
                            MY_MAIL,
                            msg=f'Subject: {subject}\n\n{body.encode("utf-8")}'
                            )
