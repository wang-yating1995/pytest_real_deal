import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestCookies():
    def setup_method(self,method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()

    def teardown_method(self,method):
        self.driver.quit()

    def test_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        db = shelve.open("cookies")
        # db['cookies'] = self.driver.get_cookies()
        cookies = db['cookies']
        for cookie in cookies:
            if 'expire' in cookie.keys():
                cookie.pop('expire')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(3)
