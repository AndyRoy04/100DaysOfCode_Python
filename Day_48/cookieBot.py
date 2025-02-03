# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# chrom_options = webdriver.ChromeOptions()
# chrom_options.add_experimental_option('detach', True)

# driver = webdriver.Chrome(options=chrom_options)
# driver.get('https://orteil.dashnet.org/experiments/cookie/')

# cookie = driver.find_element(By.ID, 'cookie')

# money = driver.find_element(By.ID, 'money').text
# store = driver.find_elements(By.CLASS_NAME, 'grayed')[:-1]
# store.reverse()
# item_price = []

# timeout = time.time() + 5
# five_mins = time.time() + 5*60
# # print(timeout)
# # items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
# # item_ids = [item.get_attribute("id") for item in items]
# # print(item_ids)
# for items in store:
#     price = items.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
#     item_price.append(int(price))
# # print(item_price)
# # print(store[4])


# location = 0
# while True:
#     cookie.click()
#     if time.time() >  timeout:
#         for amount in item_price:
#             if int(money) >= amount:
#                 location = item_price.index(amount)
#                 # break
#         store[location].click()
#         timeout += 5
        
#     if time.time() > five_mins:
#         cookies_second = driver.find_element(By.ID, 'cps').text
#         print(cookies_second)    
#         break
        
# # # print(item_price)
# # driver.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]   

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    # if time.time() > five_min:
    #     cookie_per_s = driver.find_element(by=By.ID, value="cps").text
    #     print(cookie_per_s)
    #     break