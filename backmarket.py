from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, time, csv, re 

PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(PATH)

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.backmarket.fr/fr-fr?gclid=CjwKCAjwmYCzBhA6EiwAxFwfgNeDq5kg-493dgvONlVjY_KmGIZB2cTsgY9s6D0WYCm8K6ggLYx-2RoC6sAQAvD_BwE&utm_campaign=FR_SA_SHOP_G_GEN_Others_PMAX_CSS&utm_medium=cpc&utm_source=google")
    wait = WebDriverWait(driver, 10)
    search = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search.send_keys("iphone")
    search.send_keys(Keys.RETURN)
    print(driver.title)
    time.sleep(60)  
except Exception as e:
    print(f"An error occurred: {e}")

