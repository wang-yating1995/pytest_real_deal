from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.get("https://home.testing-studio.com/"
        self.driver.get("https://www.baidu.com/")
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # self.driver.find_element(By.XPATH,'//*[@id="ember31"]/a').click()
        #
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="ember31"]/a')))
        # self.driver.find_element(By.XPATH,'//*[@id="ember33"]/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('霍格沃兹测试学院')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()
        time.sleep(5)

