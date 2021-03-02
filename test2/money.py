# -*- coding: utf-8 -*-
# def logger(func):
#     def wrapper(*args,**kw):
#         print("我准备开始执行{}函数了：".format(func.__name__))
#         func(*args,**kw)
#         print("我执行完啦。")
#     return  wrapper
# @logger
# def add(x,y):
#     print(f"{x}+{y}={x+y}")
# add(100,25)

def sag_hello(contry):
    def wrapper(func):
        def deco(*args,**kwargs):
            if contry =='china':
                print("你好啊！")
            elif contry == "america":
                print("hello!")
            else:
                return
            # 真正执行函数的地方
            func(*args,**kwargs)
        return deco
    return wrapper
xiaoming()
print("-----")
jack()