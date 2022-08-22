import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestAlert():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        print(self.driver.page_source)
        self.driver.switch_to.frame('iframeResult')
        element_drag = self.driver.find_element(By.XPATH,'//*[@id="draggable"]')
        element_drop = self.driver.find_element(By.XPATH,'//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(element_drag,element_drop)
        action.perform()
        # time.sleep(5)
        self.driver.switch_to.alert.accept()
        # time.sleep(5)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.page_source)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[1]/button[3]').click()
        time.sleep(5)

