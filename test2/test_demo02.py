# -*- coding: utf-8 -*-


from selenium import webdriver
import time
from time import sleep


class TestTestcase():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testcase(self):
        self.driver.get("https://ceshiren.com/")
        sleep(3)

    def test_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        sleep(3)


'''
复用已有浏览器
chrome --remote-debugging-port=9222
python
hrome_arg=webdriver.ChromeOptions()
chrome_agr.debugger_address='127.0.0.1:9222'
self.driver=webdriver.Chrome(options=chrome_arg)
'''
