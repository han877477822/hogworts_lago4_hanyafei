# -*- coding: utf-8 -*-
num=0
while True:
    n = int(input('请猜数字：'))
    if n == 7:
        print('爷爷奖励葫芦娃一个苹果')
        break
    elif n < 7:
        print("太小了")
    elif n>7:
        print("太大了")
    # num+=1

# age = int(input('请输入你的年龄:'))
# if age >= 18:
#     pass
# else:
#     print('你未成年，不得进入网吧')
# for  i  in range(1,10):
#     if i == 8:
#         continue
#     print(i)
