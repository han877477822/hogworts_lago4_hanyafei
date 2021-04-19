# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# option = Options()
# option.debugger_address = "127.0.0.1:9222"
# driver = webdriver.Chrome(options=option)
# driver.get("https://www.baidu.com/")
# driver.find_element(By.ID, "kw").send_keys("韩亚飞")
class TestWX:
    def setup(self):
        option = Options()
        # 注意 9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://www.baidu.com/")

    # def teardown(self):
    #     self.driver.quit()
    # chrome --remote-debugging-port=9222

    def test_case1(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("feiji")
        self.driver.find_element(By.CSS_SELECTOR,".hot-refresh-text").click()
        pass

