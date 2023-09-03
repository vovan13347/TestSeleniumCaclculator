

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCalculator(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(options)
       
    def test_get_url(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        WebDriverWait(driver, 3).until(EC.title_is("KALKPRO.RU калькулятор онлайн ➔ ТОЧНЫЙ и бесплатный расчет процентов, степеней, корней, дробей"))
        
    def test_buttons_are_clickable(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"7").click()
        time.sleep(3)
        driver.find_element(By.NAME,"+").click()
        time.sleep(3)
        driver.find_element(By.NAME,"2").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 9)
        time.sleep(3)
    
    def test_buttons_are_clickable_2(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"4").click()
        driver.find_element(By.NAME,"5").click()
        time.sleep(3)
        driver.find_element(By.NAME,"-").click()
        time.sleep(3)
        driver.find_element(By.NAME,"2").click()
        driver.find_element(By.NAME,"5").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 20)
        time.sleep(3)
    
    def test_buttons_are_clickable_3(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"9").click()
        time.sleep(3)
        driver.find_element(By.NAME,"*").click()
        time.sleep(3)
        driver.find_element(By.NAME,"8").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 72)
        time.sleep(3)
    
    def test_buttons_are_clickable_4(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"1").click()
        driver.find_element(By.NAME,"8").click()
        time.sleep(3)
        driver.find_element(By.NAME,"/").click()
        time.sleep(3)
        driver.find_element(By.NAME,"6").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 3)
        time.sleep(3)
    
    def test_buttons_are_clickable_5(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"4").click()
        driver.find_element(By.NAME,"9").click()
        time.sleep(3)
        driver.find_element(By.NAME,"sqrt").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 7)
        time.sleep(3)
    
    def test_buttons_are_clickable_6(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"2").click()
        time.sleep(3)
        driver.find_element(By.NAME,"^").click()
        time.sleep(3)
        driver.find_element(By.NAME,"6").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 64)
        time.sleep(3)
    
    def test_buttons_are_clickable_7(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"9").click()
        driver.find_element(By.NAME,"0").click()
        time.sleep(3)
        driver.find_element(By.NAME,"*").click()
        time.sleep(3)
        driver.find_element(By.NAME,"5").click()
        driver.find_element(By.NAME,"0").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Percent").click()
        time.sleep(3)
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(int(value), 45)
        time.sleep(3)
    
    def test_buttons_are_clickable_8(self):
        driver = self.driver
        driver.get("https://kalkpro.ru/")
        driver.find_element(By.NAME,"4").click()
        time.sleep(3)
        driver.find_element(By.NAME,"reciproc").click()
        time.sleep(3)
        driver.find_element(By.NAME,"Result").click()
        value = driver.find_element(By.CLASS_NAME,"display-values").text
        self.assertEqual(float(value), 0.25)
        time.sleep(3)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


