# -*- coding: utf-8 -*-
import shelve
#复用浏览器
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX():
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    #def teardown(self):
        #self.driver.quit()

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_id("menu_contacts").click()
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(3)
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [{'domain': '.qq.com', 'expiry': 1617016834, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851074632985'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851074632985'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'gdCsWJfpFgV8lOMIpjZC4XwSiaNhDpSx7WEK0zapnGy0vkndoamUGKj9rH9vTjkM'}, {'domain': '.qq.com', 'expiry': 1617103174, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.247466598.1617013257'}, {'domain': 'work.weixin.qq.com', 'expiry': 1617044791, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '95ipb4l'}, {'domain': '.qq.com', 'expiry': 1680088774, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.520312714.1614650973'}, {'domain': '.work.weixin.qq.com', 'expiry': 1619608777, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1617084284, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True, 'value': 'o2811614623'}, {'domain': '.qq.com', 'expiry': 1617084284, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True, 'value': '00010000b6f502f4fbc6f37920bbdff613a1159a2814c7b29846e91d2a028cd0872be9eccacaa9d0f60d0c35'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1617013257'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '40080481861255889'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5006256'}, {'domain': '.qq.com', 'expiry': 1640654508, 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': True, 'value': '58961609118507367'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '5308306432'}, {'domain': '.qq.com', 'expiry': 1617084283, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': True, 'value': '2811614623'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646186954, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1640654508, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': True, 'value': '1609118507367'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324986148409'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3549120376'}, {'domain': '.qq.com', 'expiry': 1923475227, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '1_2811614623'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'wblIIsl5P_5sJxrg6eoxAIu2dCI7sSw8cWyLGqG4P2P5MUnAI5MlOYHe9MftLQpERJph5ARLgwbHsfEpmQ0hir0xVWipzlitpTzOmHP3nmaKWfsWXfNTP44mupksl7Y2IX_T55uGMj5i8PWpoZEnCusIEB6cpR5Y40Jzf3xZ0Is5hywInWCRXmn1qyFF_N89fFZoKVDuxBzt82-RlaTG6LouZhVlwEQa0dsrLzYgnheecqUqTPHdbKUGCkgLU3Y93GI8MmTom3uR41ixBv5Mwg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1648549256, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614650978,1614907970,1616581817,1617013257'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1622426972, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'secure': True, 'value': '1.1.1311616009.1614650972'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '2811614623'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '93edcb4eb2ab5433ad0d62422dffe30998a833ce4c4d74603563563d73545509'}, {'domain': '.qq.com', 'expiry': 2147483645, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': '7eihLYWHmj'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)
        self.driver.maximize_window()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)

        # # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(4)

    # def test_case2(self):
    #     db = shelve.open('cookies')
    #     cookies = db['cookie']
    #     db.close()
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     sleep(2)
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     self.driver.maximize_window()
    #
    #     self.driver.refresh()
    #     sleep(4)
