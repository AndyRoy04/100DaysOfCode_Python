from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SIMILAR_ACCOUNT = ''
USERNAME = ''
PASSWORD = ''

class InstaFollower():
    def __init__(self):
        # Initializing a chrom browser
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        name_field = self.driver.find_element(By.NAME, value='username')
        name_field.send_keys(USERNAME)
        password_field = self.driver.find_element(By.NAME, value='password')
        password_field.send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button/div').click()
        time.sleep(7)
        
        save_login = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login:
            save_login.click()
        time.sleep(2)
    
    def find_follower(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        # self.driver.find_element(By.LINK_TEXT, value=' following').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]').click()
    
    def follow(self):
        time.sleep(3)
        follow_account = self.driver.find_element(By.CSS_SELECTOR, value=".x78zum5 button ._ap3a").click()
        time.sleep(2)
        print(follow_account)        
        # for account in follow_account:
        #     account.click()
        #     time.sleep(1)
            
    
bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()