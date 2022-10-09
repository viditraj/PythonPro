# selenium 3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
timeout = time.time() + 10

while True:
    cookie.click()
    score_string = driver.find_element(By.ID, 'money').text
    score = int(score_string.replace(',', ''))
    if time.time() > timeout:
        cookie_rate = driver.find_element(By.ID, 'cps').text
        print(cookie_rate)
        if score > 123456789:
            time_machine = driver.find_element(By.ID, 'buyTime machine')
            time_machine.click()
        elif 123456789 > score > 1000000:
            Portal = driver.find_element(By.ID, 'buyPortal')
            Portal.click()
        elif 1000000 > score > 50000:
            Alchemy = driver.find_element(By.ID, 'buyAlchemy lab')
            Alchemy.click()
        elif 50000 > score > 7000:
            Shipment = driver.find_element(By.ID, 'buyShipment')
            Shipment.click()
        elif 7000 > score > 2000:
            Mine = driver.find_element(By.ID, 'buyMine')
            Mine.click()
        elif 2000 > score > 500:
            Factory = driver.find_element(By.ID, 'buyFactory')
            Factory.click()
        elif 500 > score > 100:
            Grandma = driver.find_element(By.ID, 'buyGrandma')
            Grandma.click()
        elif score > 100:
            Cursor = driver.find_element(By.ID, 'buyCursor')
            Cursor.click()
        timeout = time.time() + 10

