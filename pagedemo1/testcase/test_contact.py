# -*- coding: utf-8 -*-
from pagedemo1123.page.main_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        # 定义一个变量赋值index 下面的
        name = "a-009"
        account = "a8090s"
        phonenum = "13589067747"
        addmemberpage = self.index.click_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = self.index.click_add_member().get_member()
        # result = self.index.click_add_member().add_member()
        print(result)
