# # -*- coding: utf-8 -*-
#
# import pandas as pd
#
# #通过Series存储每个英雄的基本信息
# #创建Series
# s1 = pd.Series([1001,'鲁班','18','150.00','男'])
# s2 = pd.Series([1002,'小乔','19','167.00','女'])
# s3 = pd.Series([1003,'关羽','30','180.00','男'])
# s4 = pd.Series([1004,'蔡文姬','20','160.00','女'])
# s5 = pd.Series([1005,'兰陵王','22','165.00','男'])
#
# series_list=[s1,s2,s3,s4,s5]
#
# #创建一个DataFrame对象存储通讯录
# df=pd.DataFrame(series_list)
#
# # 打印刚刚构造的DataFrame
# print(df)
# print(12)



import json

a = {"title": "今天是学习爬虫的第1天！", "date":"2019.10.1", "content":"今天是学习爬虫的第1天！我学习了爬虫基础啦！"}
b = json.dumps(a)
c = json.loads(b)
print(type(a))
print(c)

print(type(c))





















