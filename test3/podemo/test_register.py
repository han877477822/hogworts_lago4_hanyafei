# -*- coding: utf-8 -*-
from test3.podemo.main import MainPage


class TestRegister:
    def setup(self):
        self.main=MainPage()

    def test_regist(self):
        result = self.main.goto_register().register()
        print(type(result))
        #视频看到45分30秒，下面要复用浏览器了