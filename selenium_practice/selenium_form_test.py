import pytest
from selenium import webdriver



class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()

    def test_form(self):
        pass
