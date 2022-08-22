import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class TestTsouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get("http://www.baidu.com")
        element_input = self.driver.find_element(By.ID,'kw')
        element_search = self.driver.find_element(By.ID,'su')
        element_input.send_keys('selenium测试')
        action = TouchActions(self.driver)

        action.tap(element_search)
        action.perform()

        action.scroll_from_element(element_input,0,10000).perform()
        time.sleep(3)


