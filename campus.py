from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
s = Service('C:/Users/rahul/OneDrive/Desktop/chromedriver.exe')

driver = webdriver.Chrome(service= s)

driver.get('https://google.com')
time.sleep(2)

user_input = driver.find_element(by = By.XPATH , value = '//*[@id="APjFqb"]')
user_input.send_keys('Campusx')

time.sleep(1) 

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by = By.XPATH , value='//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a')
link.click()
time.sleep(2)

link2 = driver.find_element(by=By.XPATH , value='//*[@id="1668425005116"]/span[2]/a')
link2.click()
time.sleep(12000)