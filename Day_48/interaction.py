from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrom_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')

# print(f'Total articles: {article_count.click()}')
Afro = driver.find_element(By.LINK_TEXT, value='African Americans')
# Afro.click()
search = driver.find_element(By.NAME, value='search')
search.send_keys("Python", Keys.ENTER)

driver.quit()