# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test3.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member(self, name, account, phonenum):
        # name = "aa_0"
        # account = "aa_harts"
        # phonenum = "13362345678"
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_memeber(self,value):
        locator =(By.CSS_SELECTOR,".ww_checkbox")
        self.wait_for_click(locator)
        #WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # find_elements返回的是元素列表[element1,element2]
        # titles=[]
        # for element in elements:
        # #    titles.append(element.get_attribute("title"))
        # elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # titles = [element.get_attribute("title") for element in elements]
        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)
            page=self.find(By.CSS_SELECTOR,".ww_pageNav_info_text").text
            num,total = page.split("/",1)
            if int(num)==int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR,".ww_commonImg.ww_commonImg_PageNavArrowRightNormal").click()
        return titles_total
