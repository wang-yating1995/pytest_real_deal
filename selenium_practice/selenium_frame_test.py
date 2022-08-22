import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrame():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH,'//*[@id="s-top-loginbtn"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__regLink"]').click()
        time.sleep(5)
        windowall = self.driver.window_handles
        window1 = self.driver.current_window_handle
        self.driver.switch_to.window(windowall[-1])
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__userName"]').send_keys('quantang')
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__phone"]').send_keys('15659658891')
        time.sleep(5)
        self.driver.switch_to.window(window1)
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').send_keys('15659658891')
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys('123456')
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()
        time.sleep(5)

    def test_frame02(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        e1 = self.driver.find_element(By.XPATH,'//*[@id="draggable"]')
        print(e1.text)
        e2 = self.driver.find_element(By.XPATH,'//*[@id="droppable"]')
        print(e2.text)
