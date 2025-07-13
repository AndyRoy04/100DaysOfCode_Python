from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initializing a chrom browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4258380112&f_AL=true&geoId=101174742&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true')

# Loads automatically the linked in page and clicks on the signin button
driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button').click()

# filling the email and password, then clicking the sign in button
email_input = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email_input.send_keys('codingjourney25@gmail.com')
password_input = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password_input.send_keys('codingjourney25@')

driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button').click()
time.sleep(2)

# clicking on easy apply when the page loads
driver.find_element(By.XPATH, value='//*[@id="jobs-apply-button-id"]').click()
time.sleep(2)

# Filling the phone number
numbe_input = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4258380112-21462341092-phoneNumber-nationalNumber"]')
numbe_input.send_keys('2345678910')

# Clicking next button twice
driver.find_element(By.CLASS_NAME, value='artdeco-button--primary').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, value='artdeco-button--primary').click()
time.sleep(2)

# FIlling in the blanks spaces
input_fields = driver.find_elements(By.CLASS_NAME, value='artdeco-text-input--input')

for fields in input_fields:
    fields.send_keys('2')
    
# Clicking the review button
driver.find_element(By.CLASS_NAME, value='artdeco-button--primary').click()
time.sleep(2)

# Clicking Submit button
driver.find_element(By.CLASS_NAME, value='artdeco-button--primary').click()

# driver.quit()

