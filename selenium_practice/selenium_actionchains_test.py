import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()

    def test_action_chains01(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        actions = ActionChains(self.driver)
        element_click_me = self.driver.find_element(By.XPATH,'/html/body/form/input[3]')
        element_double_click = self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        element_ringht_click = self.driver.find_element(By.XPATH,'/html/body/form/input[4]')
        actions.click(element_click_me)
        actions.double_click(element_double_click)
        actions.context_click(element_ringht_click)
        actions.perform()
        time.sleep(5)
        print(self.driver.find_element(By.XPATH,'/html/body/form/textarea').get_attribute('value'))

    def test_action_chains02(self):
        self.driver.get('https://www.baidu.com')
        actions = ActionChains(self.driver)
        element_hover = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        actions.move_to_element(element_hover)
        actions.perform()
        time.sleep(5)

    def test_action_chains03(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        action = ActionChains(self.driver)
        element_drag = self.driver.find_element(By.ID,'dragger')
        element_drop = self.driver.find_element(By.XPATH,'/html/body/div[2]')
        action.drag_and_drop(element_drag,element_drop).perform()
        time.sleep(5)

    def test_action_chains04(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        action = ActionChains(self.driver)
        element01 = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        element01.click()
        action.send_keys('username').pause(1).perform()
        # action.send_keys(Keys.SPACE).pause(1)
        # action.send_keys('tom').pause(1)
        # action.send_keys(Keys.BACK_SPACE).perform()
        # time.sleep(3)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).pause(1).perform()
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).pause(1).perform()
        element02 = self.driver.find_element(By.XPATH,'/html/body/label[2]/table/tbody/tr/td[2]/input')
        element02.click()
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).pause(1).perform()
        # action.perform()
        time.sleep(3)
