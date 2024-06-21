import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import page 

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setup")
        PATH = "C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
        service = Service(PATH)

        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://python.org")
   
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()


        
    def tearDown(self) :
        self.driver.close()

if __name__ == "__main__":
    unittest.main()