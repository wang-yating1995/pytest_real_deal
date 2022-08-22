import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestJs():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        # self.driver.find_element(By.ID,'su').click()
        self.driver.execute_script("return document.getElementById('su')").click()
        time.sleep(5)
        self.driver.execute_script("return document.documentElement.scrollTop=10000")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="page"]/div/a[10]').click()
        time.sleep(5)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_js_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        time.sleep(5)
        #用js去掉readonly属性，然后直接输入日期文本
        date_js = 'document.getElementById("train_date").removeAttribute("readonly")'
        self.driver.execute_script(date_js)
        date_js1 = 'document.getElementById("train_date").value="2022-09-14"'
        self.driver.execute_script(date_js1)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
        time.sleep(5)
