# -*- coding: utf-8 -*-



from selenium.webdriver.common.by import By

from test3.podemo1.page.addmember_page import AddMemberPage
from test3.podemo1.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    def click_add_member(self):
        self.find(By.CSS_SELECTOR, '.ww_indexImg.ww_indexImg_AddMember + span.index_service_cnt_item_title').click()
        # self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_item_title：nth-child(1)').click()
        return AddMemberPage(self.driver)
