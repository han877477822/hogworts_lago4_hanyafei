# -*- coding: utf-8 -*-
from time import time

#time.sleep(3)#强制等待3秒
#self.driver.implicitly_wait(3) 设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没有出现就抛出异常
#显示等待--在代码中定义等待条件，当条件发生时才继续执行代码 'WebDriverWait'配合unitl()和until_not()方法，根据判断条件进行等待
#程序每隔一段时间（默认是0.5秒）进行条件判断，如果条件成立，则执行下一步，否则继续等待，直到超过设置的最长时间
# json1={"刘备":50,"张飞":47,"关羽":49}
# del json1["刘备"]
#
# print(json1.values())
a=[]
b=[1,3,3,4]
a.extend(b)
c=[2,3,3,4]
a.extend(c)
print(a)