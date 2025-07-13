from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_UP = 150
PROMISED_DOWN = 450
TWITTER_EMAIL = ''
TWITTER_USERNAME = ''
TWITTER_PASSWORD = ''


class InternetSpeedTwitterBot():
    def __init__(self):
        # Initializing a chrom browser
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, value='test-mode-multi').click()  # clicking the GO button
        time.sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text

        
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(3)
        # feeling and clicking on all proceed buttons
        email_field = self.driver.find_element(By.TAG_NAME, value='input')
        email_field.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(3)
        username = self.driver.find_element(By.TAG_NAME, value='input')
        username.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(5)
        
        # Posting on twitter
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(3)
        tweet = self.driver.find_element(By.CLASS_NAME, value='public-DraftStyleDefault-block')
        tweet_text = f'Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up'
        tweet.send_keys(tweet_text)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span').click()
        
        # time.sleep(2)
        self.driver.quit()


# Innitializing the object and calling the two methods
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()