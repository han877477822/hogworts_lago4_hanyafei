# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        option = Options()
        # 注意 9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()
#chrome --remote-debugging-port=9222

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(3)
