import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFileLoad():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_fileload(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.XPATH,'//*[@id="form"]/span[1]/span[1]').click()
        time.sleep(2)
        e = self.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[2]/input')
        e.send_keys('D:\稿定测试素材\平面/0b7ad604-3fe3-49f1-9355-dae12a35c5f23868.png')
        time.sleep(5)


