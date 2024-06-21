from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, time, csv, re
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("http://www.olympedia.org/statistics/medal/country")


year = driver.find_element(By.ID,'edition_select')

year_opt = year.find_elements(By.TAG_NAME,'option')

gender = driver.find_element(By.ID,'athlete_gender')

gender_opt = gender.find_elements(By.TAG_NAME,'option')

print(year_opt[29].get_attribute('text'))

usa_lst = []

for gender in gender_opt[1:]:
    gender.click()
    time.sleep(2)
    gender_val = gender.get_attribute('text')

    for year in year_opt[2:]:
        year.click()
        time.sleep(1)

the_soup = BeautifulSoup(driver.page_source,'html.parser')
try:
    year_val = year.get_attribute('text')
    head = the_soup.find(href=re.compile('USA'))
  
    medal_values = head.find_all_next('td',limit=5)
    val_lst = [x.string for x in medal_values[-4:]]
            
except:
    val_lst = ['0' for x in range(4)]

    val_lst.append(gender_val)
    val_lst.append(year_val)
    usa_lst.append(val_lst)
driver.quit()

print(usa_lst[30])
print(usa_lst[31])


try:
    output_f = open('output.csv', 'w', newline='')
    output_writer = csv.writer(output_f)
    for row in usa_lst:
        output_writer.writerow(row)

except:
    pass
finally:
    output_f.close()
    print('done')