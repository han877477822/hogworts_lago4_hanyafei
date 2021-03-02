# -*- coding: utf-8 -*-
# for i in range(1,10):
#     for l in range(1,i+1):
#         print('%d X %d = %d   ' % (i,l,i*l),end="")
#     print(" ")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print( '%dX%d=%d '%(j,i,i*j),end=" ")
#     print("")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
#     print('  ')
# list=[523, 435, 712, 566, 613, 675, 620, 689, 643]
# list.sort(reverse=True)
# print(list)
# list=[10000,8500,9000,7000,8000,8000,9000,20000,15000,16000,5000]
# sum = 0
# average = 0
#
# for i in (list):
#     sum+=i
# average=sum/len(list)
#
# print(average)
# def fun(x):
#     y =30+11*x
#     return (y)
# f=fun(1)
# print(f)
# food=input("请选择你想吃的食物：")
# def cant(x):
#     str="你好，欢迎来到餐厅，您的点餐为："+x
#     return str
# src=cant(food)
# print(src)
# import random
# foodten = ['蛋挞','鸡翅','薯条']
# def order(money):
#     if money > 99:
#         a = random.choice(foodten)
#         return a,'冰激淋'
#     elif 69 < money < 99:
#         b = random.choice (foodten)
#         return b
#     else:
#         return '不好意思，您的消费达不到优惠活动'
# print(order(50))
# print(order(70))
# print(order(130))
# name = input('请输入姓名')
# year = int(input('请输入工作年限，数字'))
# name = input('请输入姓名')
# year = int(input('请输入工作年限，数字'))
# def money(name,year):
#     if year<1:
#         print('%s你好，今年你拿1000元奖金' %name)
#     elif 1<=year<3:
#         print('%s你好，今年你拿3000元奖金' %name)
#     else:
#         print('%s你好，今年你拿10000元奖金' %name)
# money(name,year)
'''现在KFC餐厅的奖金激励政策变了，变成如下：
1.工作时间＜1年的，发放1000元
2.工作年限≥1年但<3年的，发放奖金3000*年数（年数输入时只输入整数）如1年半为 3000*1 = 3000
3.工作年限≥3年的，发放奖金5000*年数（年数输入时只输入整数） 如3年为 5000*3 = 15000
2定义两个函数第一个函数功能为根据工作年数返回奖金额，第二个函数功能为打印出'XX员工来了X年，获得奖金XXX元'。
比如输入姓名 ‘老王’，年限‘3’；就会打印出“老王来了3年，获得奖金15000元”。'''
# name = input('请输入姓名')
# year = int(input('请输入工作年限，数字'))
# money=0
# def bonus(year):
#    if year<1:
#      money = 1000
#    elif 1<=year<3:
#      money = 3000*year
#    else:
#      money = 5000*year
#    return money
#
# def res(name,year):
#    cash = bonus(year)
#    print('%s来了%d年,获得奖金%d元' %(name,year,cash))
# res(name,year)
# import math
# a=math.ceil(0.01)
# # print(a)
# import math
# # 配送调配计算
# # 设置默认参数
# def calculate_job(size=1,person=None,num=None):
#     if(person !=None)and(num==None):
#          #配送次数计算过程
#         num = math.ceil(size * 100 / 20/person)
#         print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' %(size,person,num))
#     elif(person==None)and(num!=None):
#         #快递员数计算过程
#         person = math.ceil(size *100 /20/ num)
#         print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' %(size,num,person))
# # calculate_job(size=1.5,person=2)
#
#
# # calculate_job(size=0.5,num=1)
# import time
# def index():
#       time.sleep(2)
#       print("welcome to my world")
#
# start = time.time()
# print(start)
# index()
# end = time.time()
# print("run time is %s" %(end - start))
# def test():
#     time.sleep(3)
# a="hello world 你好"
# print(a)
# print(a.title())

import requests

# 引用requests库

res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplac'
                         'e=txt.yqq.song&searchid=65805191174562925&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&'
                         'n=10&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&'
                         'outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')

# 调用get方法，下载这个字典

# json_music = res_music.json()

# 使用json()方法，将response对象，转为列表/字典

print(type(res_music.encoding))

# 打印json_music的数据类型











