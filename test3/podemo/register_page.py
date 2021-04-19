# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self,dirver:WebDriver):
        self.driver=dirver
    def register(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("aaaa")
        self.driver.find_element(By.ID,"register_tel").send_keys("13456789876")
        self.driver.find_element(By.ID,"manager_name").send_keys("aaaa")
        # input  comany namemanager_name
        # input phonenum
        # input register
        return True
