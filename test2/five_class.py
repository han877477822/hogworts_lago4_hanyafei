# -*- coding: utf-8 -*-
import time
import random

# 也可合并写成一行：import time,random
freeLi_score = 0
# 存放李逍遥赢的局数。
BOSS_score = 0
# 存放拜月教主赢的局数

while True:
    for i in range(1, 4):
        time.sleep(1)  # 让局与局之间有较明显的有时间间隔
        print(' \n——————现在进行第' + str(i) + '局，3，2，1，go!——————')  # 作为局的标记

        # 生成随机属性
        freeLi_life = random.randint(100, 150)  # “freeLi_life” 代表李逍遥血量
        freeLi_attack = random.randint(20, 30)  # “freeLi_attack” 代表李逍遥攻击
        BOSS_life = random.randint(100, 150)  # “BOSS_life” 代表拜月教主血量
        BOSS_attack = random.randint(20, 30)  # “BOSS_attack” 代表拜月教主攻击

        # 展示双方角色的属性
        print('【李逍遥】\n' + '血量：' + str(freeLi_life) + '\n攻击：' + str(freeLi_attack))
        # freeLi_life和freeLi_attack的数据类型都是整数，所以拼接时需要先用str()转换
        print('------------------------')
        time.sleep(1)
        # 暂停一秒再执行后续代码
        print('【拜月教主】\n' + '血量：' + str(BOSS_life) + '\n攻击：' + str(BOSS_attack))
        print('------------------------')

        # 自动PK阶段
        while (freeLi_life > 0) and (BOSS_life > 0):
            freeLi_life = freeLi_life - BOSS_attack
            BOSS_life = BOSS_life - freeLi_attack

            print('李逍遥发起了攻击，【拜月教主】剩余血量' + str(BOSS_life))
            # freeLi_life是整数，所以拼接时要先用str()转换
            print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量' + str(freeLi_life))
            print('------------------------')
            time.sleep(2)
            # 为了体现出战斗回合，这里停顿2秒

        # 打印战果
        if freeLi_life > 0 and BOSS_life <= 0:
            freeLi_score = freeLi_score + 1
            print('拜月教主挂了，李逍遥赢了')
        elif freeLi_life <= 0 and BOSS_life > 0:
            BOSS_score = BOSS_score + 1
            print('悲催，拜月教主把李逍遥干掉了！')
        else:
            print('哎呀，李逍遥和拜月教主同归于尽了！')

    if freeLi_score > BOSS_score:
        time.sleep(1)
        print('【 大战3个回合：李逍遥赢了！】')
    elif BOSS_score > freeLi_score:
        print('【大战3个回合：李逍遥输了！】')
    else:
        print('【大战3个回合：平局！】')

    choose = input('你敢与我再次决战吗？？回答:再战/结束')
    if choose == '结束':
        break
