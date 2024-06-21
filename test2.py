from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("http://www.techwithtim.net")

link = driver.find_element(By.LINK_TEXT, "Tutorials")
link.click()

try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "From basic to advanced. Learn python programming."))
    )
    elem.click()
    driver.back()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
