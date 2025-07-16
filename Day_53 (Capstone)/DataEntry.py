from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
zillow_clone = response.text

soup = BeautifulSoup(zillow_clone, 'html.parser')

# ---------------- BEAUTIFULSOUP, SCRAPPING ZILLOW WEBSITE -------------------------- #
# getting the address, price and link to properties
addresses = soup.find_all(name='address')
prices = soup.find_all(name='span', class_="PropertyCardWrapper__StyledPriceLine")
links = soup.find_all(name='a', class_="StyledPropertyCardDataArea-anchor")

# Converting the address, price and link to properties to a list
address_list = []
price_list = []
link_list = []

for address in addresses:
    address = address.text.replace(" |", "")
    address = address.replace("\n", "").strip()
    # print(real_address)
    address_list.append(address)
    
for price in prices:
    price = price.text.replace("+ 1", "").replace('/mo', "").replace("+", "").replace(" ", '').replace("bd", "")
    price_list.append(price)

for link in links:
    link = link.get("href")
    link_list.append(link)

# -------------- SELENIUM WEBFORM FILLING ------------------
# Initializing a chrom browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# Looping through the list of available properties and filling the google form with the information
for i in range(len(link_list)):
    driver.get("https://forms.gle/3KHwtnczPHXtkdwr7")  # link to google forms
    adress_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value="//span[contains(text(), 'Submit')]")
    
    adress_field.send_keys(address_list[i])
    price_field.send_keys(price_list[i])
    link_field.send_keys(link_list[i])
    submit_button.click()
    time.sleep(1)
    
driver.quit()
    