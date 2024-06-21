from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import os, time, csv, re  # Not used in this example

PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(PATH)

try:
    driver = webdriver.Chrome(service=service)

    driver.get("https://backmarket.fr/")

    # Improved search bar element handling using WebDriverWait and error handling
    wait = WebDriverWait(driver, 50)
    try:
        search = wait.until(EC.presence_of_element_located((By.ID, "autocomplete-0-input")))
        search.send_keys("iphone")
        search.send_keys(Keys.RETURN)
        print(driver.title)
    except StaleElementReferenceException:
        print("Search bar element might have changed. Trying to refresh...")
        search = driver.find_element(By.ID, "autocomplete-0-input")  # Refresh element reference
        search.send_keys("iphone")
        search.send_keys(Keys.RETURN)
        print(driver.title)  # Print after potential refresh

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
