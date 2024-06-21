from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(1)

for i in range(100):
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    count = cookie_count.text  # Move this line inside the loop
    print(count)
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(2)]

    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
   

driver.quit()