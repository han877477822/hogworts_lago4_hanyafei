# -*- coding: utf-8 -*-
# 这段代码在本地执行

from selenium import webdriver #从selenium库中调用webdriver模块
import selenium

import time



dr = webdriver.Chrome()
# 设置引擎为Chrome，从本地打开一个Chrome浏览器

dr.get('https://xiaoke.kaikeba.com/example/X-Man/') # 访问页面

time.sleep(2) # 等待两秒

label = dr.find_element_by_class_name('form-teacher') # 根据类名找到元素

print(type(label)) # 打印label的数据类型

print(label.get_attribute('type')) # 获取type这个属性的值

dr.close() # 关闭浏览器