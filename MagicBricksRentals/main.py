from selenium import webdriver
from selenium.webdriver.common.by import By
from GoogleFormFiller import fill_form
import pandas as pd
city = input("Enter city name you are currently looking in: ")
maxBudget = input("Enter max budget: Rs.")

URL = f'https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=1,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Residential-House,Villa&cityName={city}&BudgetMax={maxBudget}'

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

driver.implicitly_wait(10)
properties_html = driver.find_elements(By.CLASS_NAME, 'mb-srp__card--title')
desc_html = driver.find_elements(By.CSS_SELECTOR, '.mb-srp__card--desc--text p')
price_html = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__price--amount')
properties = {}
for i in range(len(desc_html) - 1):
    properties[i] = {}
    properties[i]["PropertyName"] = properties_html[i].text
    properties[i]["Description"] = desc_html[i].text
    properties[i]["Price"] = price_html[i].text.replace('\n', '')
    print(properties[i])

driver.quit()
df = pd.DataFrame.from_dict(properties, orient='index')
df.to_csv('properties.csv')

#fill_form(properties)
