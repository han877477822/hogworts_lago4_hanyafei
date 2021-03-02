# -*- coding: utf-8 -*-
# import csv
#
# with open("mytest.csv",encoding='utf-8-sig')  as r:
#     print("内容如下\n")
#     reader = csv.reader(r)
#     #使用csv的reader()方法，创建一个reader对象
#     for content in reader:
#     #遍历reader对象的每一行
#         print(content)
#
# print("读取完毕！")
# import csv
# from kkb_tools import open_file
# with open("mytest1.csv",'a')  as r:
#     writer = csv.writer(r)
#     writer.writerow([41,42,43])
# print("写入完毕！")
# open_file("mytest1.csv")
# from email.mime.text import MIMEText
# import smtplib
# #把email模块与smtplib模块引入进来,我们还使用MIMEText构造了邮件内容。
# # MIMEText有三个参数：邮件内容、MIME的subtype;test/plain、编码格式
# msg = MIMEText('hello, Python auto send email', 'plain', 'utf-8')
# # 输入Email地址和口令:
# from_addr = input('请输入发件人的邮箱号码From: ')
# password = input('请输入发件人的邮箱密码Password: ')
# # 输入SMTP服务器地址:
# #QQ邮箱SMTP服务器地址：smtp.qq.com, 端口465, QQ邮箱默认的端口是25, 我们这里使用的是加密端口465。
# smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# # 输入收件人地址:
# to_addr = input('请输入收件人邮箱地址To: ')
#
# import smtplib
# server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议加密端口是465
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()          #调试级别
import csv #引入csv模块
#调用open()方法，文件名是detaillist.csv，追加模式"a", 文件名在代码中称为listfile
with open("detaillist.csv","a",newline='',encoding='GBK') as listfile:
    #使用csv.writer（）函数创建writer对象，用于写入
    writer = csv.writer(listfile, dialect='excel')
    #列表头部第一行的字段
    header = ['期次','偿还本息（元）','偿还本金（元）','偿还利息（元）']
    # 使用writer对象写入表头
    writer.writerow(header)
open_file("detaillist.csv")
