from time import sleep
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://docs.google.com/forms/d/e/1FAIpQLScjdb9MllmaBgtct5jK8KluMBW64MRGgQCkrX08yc2mX3Vy3Q/viewform"


def fill_form(properties):
    for i in tqdm(range(len(properties) - 1)):
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.implicitly_wait(10)
        sleep(5)
        title_box = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        title_box.send_keys(properties[i]["PropertyName"])
        desc_box = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
        desc_box.send_keys(properties[i]["Description"])
        price_box = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_box.send_keys(properties[i]["Price"])
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()
        driver.quit()


# properties2 = {
#     0: {
#         "PropertyName": "ViditNiwas",
#         "Description": "Home Sweet Home",
#         "Price": "6000"
#     },
#     1: {
#         "PropertyName": "ViditNiwas",
#         "Description": "Home Sweet Home",
#         "Price": "6000"
#     }
# }
#
# fill_form(properties2)
