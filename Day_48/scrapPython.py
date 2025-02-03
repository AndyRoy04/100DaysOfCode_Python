from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeping chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

all_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')
date_event = {}
index = 0

for event in all_events:
    time = event.find_element(By.CSS_SELECTOR, 'time').text
    event_name = event.find_element(By.CSS_SELECTOR, 'a').text
    complete_event = {
        'time' : time,
        'name' : event_name,
    }
    date_event[index] = complete_event
    index += 1
    
print(date_event)

driver.quit()