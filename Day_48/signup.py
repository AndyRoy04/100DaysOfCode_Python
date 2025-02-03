from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrom_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

F_name_input = driver.find_element(By.NAME, 'fName')
L_name_input = driver.find_element(By.NAME, 'lName')
Email_input = driver.find_element(By.NAME, 'email')

F_name_input.send_keys('Andy')
L_name_input.send_keys('Royinho')
Email_input.send_keys('andyroyinho@gmail.com')

button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()


# driver.quit()