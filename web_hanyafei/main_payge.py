# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_hanyafei.login_page import LoginPage
from web_hanyafei.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver =webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        #click login
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        #这个跟上面的定位是一样的  self.driver.find_element_by_css_selector()
        #进入到登录页面
        return LoginPage(self.driver)

    def goto_register(self):
        #click register
        self.driver.find_element(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()

        #进入注册页g
        return RegisterPage(self.driver)