from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

class TestTestrhome():

    def setup(self):
        # 实例化driver
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 隐式等待（全局，简化代码）,缺点：隐式等待只能查找到元素，不能判断元素是否是可点击的
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 关闭浏览器
        self.driver.quit()

    def test_testerhome(self):
        # 打开网址
        self.driver.get("https://testerhome.com/")
        # 点击社团标签
        self.driver.find_element(By.XPATH,'//*[@id="main-nav-menu"]/li[1]/a').click()
        # 点击第一篇文章
        # time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a').click()
        # time.sleep(5)
