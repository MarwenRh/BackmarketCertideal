from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup  

import os, time, csv, re  

PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(PATH)

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.backmarket.fr")

    wait = WebDriverWait(driver, 10)
    try:
        search = wait.until(EC.element_to_be_clickable((By.ID, "searchBar-input")))
        search.send_keys("iphone")
        search.send_keys(Keys.RETURN)
        print(driver.title)
    except NoSuchElementException:
        print("Search bar element not found!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
