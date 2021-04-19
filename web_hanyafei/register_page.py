# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        # input company name
        self.driver.find_element(By.ID, "manager_name").send_keys("aaa")
        # input phonenum
        self.driver.find_element(By.ID, "register_tel").send_keys("13012345678")
        # click register 点击注册
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
