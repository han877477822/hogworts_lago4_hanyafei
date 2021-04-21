# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://tptbrtctest.life.cntaiping.com/tptb/h5/tbadmin/#/rsm/exc-proj-contract")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID,"tab-account").click()
driver.find_element(By.CSS_SELECTOR,"#pane-account > div > div.comp-account-login > form > div:nth-child(1) > div > div > input").send_keys("13564390347")
driver.find_element(By.CSS_SELECTOR,".comp-smscode_send-btn").click()
driver.find_element(By.CSS_SELECTOR,"#pane-account > div > div.comp-account-login > form > div:nth-child(2) > div > div > input").send_keys("111111")
driver.find_element(By.CSS_SELECTOR,".btn-submit").click()
driver.find_element(By.XPATH,"//*[@id='master-container']/div[1]/div[2]/div/div[2]/div[2]/div[10]/div[1]/img").click()
driver.find_element(By.LINK_TEXT,"新建项目").click()
# driver.find_element(By.XPATH,"//*[@id=‘app’]/div/div/div[1]/div/div/div[1]/form/div/div[7]/button[3]/span").click()
sleep(2)
#新建项目输入一个项目的名称
pro_name="测试项目2021_01"
driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[1]/div/div/div[4]/div/div/div[2]/form/div[1]/div/div[2]/div[1]/div/div[1]/input").send_keys(pro_name)
select=Select(driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[1]/div/div/div[4]/div/div/div[2]/form/div[1]/div/div[2]/div[4]/div/div[1]/div/input"))
select.deselect_by_value("自研")
# driver.quit()
    # def test_demo1(self):
def test_cookie(self):
    # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    # sleep(3)
    # cookies = self.driver.get_cookies()
    # print(cookies)
    cookies=[]
    self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    sleep(2)
    self.driver.maximize_window()
    for cookie in cookies:
        self.driver.add_cookie(cookie)
    self.driver.refresh()
    sleep(3)
