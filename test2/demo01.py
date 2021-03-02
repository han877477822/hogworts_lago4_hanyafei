# -*- coding: utf-8 -*-
'''
1.5个标准集装箱大的快递项目，使用2位快递员配送，则需要配送次数4次
0.5个标准集装箱大的快递项目，1次配送完毕，则需要快递员数：3位'''
# import math
#
# def man(size=1,person=None,num=None):
#     if person!=None and num==None:
#         num = math.ceil(size * 100 / 20 / person)
#         print("%s个标准集装箱大的快递项目,使用%d位快递员配送,则需要配送次数%d次"%(size,person,num))
#     elif person== None and num != None:
#         person=math.ceil(size*100/20/num)
#         # person=float(size*100/20/num)
#         print("%s个标准集装箱大的快递项目,使用%d次配送完毕,则需要%s位快递员"%(size, num, person))
# man(size=1,person=5)
# man(size=2.1,num=2)
# import math
# types=int(input("请选择类型：1、配送次数计算 2、快递员人数计算。："))
# size=float(input("请输入配送物体大小:"))
# if types==1:
#     other = int(input("请输入配送人数："))
# else:
#     other = int(input("请输入配送次数:"))
# def man(types,size,other):
#     if types==1:
#         num = math.ceil(round((size * 100 / 20 / other),8))
#         print("%s个标准集装箱大的快递项目,使用%d位快递员配送,则需要配送次数%d次"%(size,other,num))
#     elif types==2:
#         person=math.ceil(round((size*100/20/other),8))
#         # person=float(size*100/20/num)
#         print("%s个标准集装箱大的快递项目,使用%d次配送完毕,则需要%s位快递员"%(size, other, person))
# man(types,size,other)
# lists = [1,3,4,5,6,7,9,2]
# # 切片
# print(lists[::-1])
# # 函数reverse 对数组进行操作
# # lists.reverse()
# # print(lists)
# # 函数reversed 返回一个迭代对象，需要list化
# print(list(reversed(lists)))
# import math
# abc=float(input("请输入："))
#
# def num():
#     if abc%1==0:
#         print(abc)
#     else:
#         num2=math.ceil(abc)
#         print(num2)
#
# num()
import math

'''出租车车费计算方式如下：
1、打车距离在3公里以内，只收起步价15元。
2、距离在3公里~15公里，每1公里加3元。
3、距离超过15公里后，每1公里加5元。
请完成计价函数。
'''
# km=float(input("请输入公里数："))
# def lucheng(km):
#     if km <= 3:
#         print("只收起步价15元")
#     elif 3<km<=15:
#         price=math.ceil(km-3)*3+15
#         print("总共需要付费：%d元"%price)
#     elif km>15:
#         price=15+(15-3)*3+math.ceil(km-15)*5
#         print("总共需要付费：%d元"%price)
# lucheng(km)
# list = ['刘备','关羽','张飞','赵云']
# del(list[3])
# print(list)
# film = {
#     '速度与激情':['强森','斯坦森'],
#     '烈火英雄':['黄晓明','杜江','杨紫'],
#     '深夜食堂':['梁家辉','刘涛'],
#     '铤而走险':['大鹏','李梦','欧豪'],
#     '使徒行者':['张家辉','古天乐']
# }
#
# star =input('你想看哪位演员的电影？')
# for i in film:
#     actors=film[i]
#     # print(i)
#     print(actors)
#     if star in actors:
#         print(star+'出演影片'+i)
# film = {
#     '速度与激情':['强森','斯坦森'],
#     '烈火英雄':['黄晓明','杜江','杨紫'],
#     '深夜食堂':['梁家辉','刘涛'],
#     '铤而走险':['大鹏','李梦','欧豪'],
#     '使徒行者':['张家辉','古天乐']
# }
#
# star =input('你想看哪位演员的电影？')
# for i in film:
#     # print(i)
#     actors=film[i]
#     if star in actors:
#         print(star+'出演影片'+i)
#
# while True:
#         try:
#             age = int(input('你今年多大了？'))
#             break
#         except ValueError:
#             print('你输入的不是数字')
# if age < 18:
#     print('不可以抽烟喝酒烫头哦')
# num = [5,6,0,10]
# for i in num:
#     except ValueError:
#         i==0
#     print(600/i)

# num = [5,6,0,10]
# for i in num:
#     if  i!=0:
#         print(600/i)

    # print (600/i)
# class Musician:
#     loveMusic = "伙我在 呆 要厅 "
#     def sing(self):
#           print('我在唱歌')
#
#
# class Starman():
#     glass="墨镜"
#     def photo(self):
#         print("与粉丝合影")
# class person:
#     def __init__(self):
#         self.glass="墨镜"
#         self.count=9
#     def intr(self):
#         print("出门必须戴%s"%self.glass)
#         print("我们有%s人"%self.count)
# fly=person()
# fly.intr()
# 创建一个类叫Maleguests，这个类中具有两个属性: sex = “M”，marriage = “False”; 类中有一个方法，叫hello方法，可以打印“各位女嘉宾好”
# class malegusts:
#     sex="M"
#     marriage="False"
#     def hello(self):
#         print("各位女嘉宾好")
# res=malegusts()
# print(res.sex)
# print(res.marriage)
# res.hello()
# '''创建一个类叫Maleguests，这个类中具有一个方法叫sayHi，sayHi方法可以介绍自己的姓名\年龄与
# 籍贯。例如“各位女嘉宾好我叫张三，我今年28岁，我来自广州”； 姓名\年龄与籍贯是可以根据需要改变的。'''
# class maleguests():
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#         print("各位女嘉宾，大家好")
#
#     def sayhi(self):
#         print(f"我叫{self.name}，我今年{self.age}岁，我来自{self.address}")
# class demo01(maleguests):
#     pass
# lianx=demo01("",18,"")
# lianx.sayhi()
# say("张三",19,"上海")
#补全代码
# class Car:
#     wheel = 4
#     def run(self):
#         print('有%d个轮子,可以飞速的行驶'%self.wheel)
# class Bmw(Car):
#     pass
# bm=Bmw()
# # print("宝马%s"%bm.wheel)
# # bm.run()
# print(isinstance(bm, Bmw))
# print(isinstance(Bmw,object))
# class Student:
#     stu_no="学号"
#     def study(self):
#         print("我会学习")
# class child:
#     studus="身份"
#     def care(self):
#         print("我会照顾父母")
# class son(Student,child):
#     pass
# mingxiao=son()
# print(mingxiao.stu_no)
# print(mingxiao.studus)
# mingxiao.study()
# mingxiao.care()
# class master:
#     def cake(self):
#         print("我可以做手抓饼")
#     def cook(self):
#         print("我可以做煎饼果子")
# class tudi(master):
#     def cook(self):
#         print("我可以做加强版的煎饼果子")
# xiao=master()
# xiao.cook()
# ming=tudi()
# ming.cook()
'''先来完成第一个简单的类，Bike类。每辆车都有基本的属性：车辆编号，使用年限，租借状态。
我们利用初始化__init__ ，让实例被创建时自动获取这些属性。'''
# class Bike:
#     def __init__(self,bike_no,old,bike_type):
#         self.bike_no=bike_no
#         self.old=old
#         self.bike_type=bike_type
#         pass
# bike=Bike(1,2,3)
# Bike=[]
# bikeA = Bike(1001, 2)
# bikeB = Bike(1002, 2)
# bikeC = Bike(1003, 1)
# Bike.append(bikeA)
# Bike.append(bikeB)
# Bike.append(bikeC)
# # bb=bikeC
# # print(bb)
# class Bike:
#     # 初始化方法 no代表车辆编号、age代表车辆年限、
#     # state代表车辆状态，0代表待租借，1代表租借中
#     def __init__(self, NO, age, state=0):
#         self.NO = NO
#         self.age = age
#         self.state = state
#
#     def __str__(self):
#         if self.state == 0:
#             status = '待租借'
#         else:
#             status = '租借中'
#         return '车辆编号%d 已经运行%d年，车辆状态：%s' % (self.NO, self.age, status)
#

# class Car(Bike):
#     def __init__(self, NO, age, name, gasoline, state=0):
#         self.NO = NO
#         self.age = age
#         self.state = state
#         self.name = name
#         self.gasoline = gasoline
# class Car(Bike):
#     def __init__(self,NO,age,name,gasoline,state=0):
#         self.NO = NO
#         self.age = age
#         self.state=state
#         self.name=name
#         self.gasoline=gasoline
# car=Car(1001,2,'Benz',95)
# print(car)
#在practice_1601.py文件中补全代码，将注释中的bytes内容放入到代码中进行解码，将解码后的内容，
# 写入到document_1601.txt文件中。 document_1601.txt的地址也写在注释中。
#b'\xe7\x9f\xa5\xe8\xa1\x8c\xe5\x90\x88\xe4\xb8\x80'
#请将上面注释中的内容放入到代码中进行解码直接粘贴即可
#document_1601.txt的地址，直接粘贴即可

# print('开课吧'.encode('gbk'))
# print('开课吧'.encode('utf-8'))
# print(b'\xbf\xaa\xbf\xce\xb0\xc9'.decode('gbk'))
# print(b'\xe5\xbc\x80\xe8\xaf\xbe\xe5\x90\xa7'.decode('utf-8'))
# from kkb_tools import open_file
# #书写你的代码

# a=b'\xe7\x9f\xa5\xe8\xa1\x8c\xe5\x90\x88\xe4\xb8\x80'.decode('utf-8')
# print(a)
# 在practice_1602.py文件中，可以接收用户所输入的任何内容，在这内容前面加上“您输入的是：”; 之后将所有的内容写入到document_1602.txt文件中。
# -*- coding: utf-8 -*-
# shur=str(input("请输入内容："))
# myfile=open(r'document_1602.txt','a')
# myfile.write(shur)
#
# myfile.close()
# my=open(r'document_1602.txt','r')
# a=my.read()
# print(a)
# myfile.close()

# open_file("document_1601.txt")


