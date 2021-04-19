# -*- coding: utf-8 -*-
# from time import time, sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# class TestTestcase():
#     def setup_method(self):
#         self.driver = webdriver.Chrome()
#     def teardown_method(self):
#         self.driver.quit()
#     def test_testcase(self):
#         self.driver.get("https://tptbrtctest.life.cntaiping.com/tptb/h5/tbadmin/#/rsm/prej-manage/")
#         sleep(5)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(4)
    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="归入各种类别的所有主题"]').click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跌的主题"]').click()