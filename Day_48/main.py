from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeping chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1')

# dollar_price = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
# cent_price = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text
random = driver.find_element(By.XPATH, value='//*[@id="mbbPopoverLink"]')
print(random.text)

# print(f'The Instant Pot Plus costs ${dollar_price}.{cent_price}')


driver.quit()