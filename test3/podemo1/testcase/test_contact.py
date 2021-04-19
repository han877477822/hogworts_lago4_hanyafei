# -*- coding: utf-8 -*-
from test3.podemo1.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index1 = IndexPage()

    def test_addcontact(self):
        name = "a_000"
        account = "aBh89ts"
        phonenum = "13900985678"
        addmemberpage = self.index1.click_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = addmemberpage.get_memeber(name)
        #result = addmemberpage.get_memeber()
        assert result
        #assert name in result
        # 1小时1分
