# -*- coding: utf-8 -*-

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
两个hp进行对比，血量剩余多的人获胜
"""
import random


def fight(enemy_hp,enemy_power):
    my_hp = 1000
    my_power = 200
    # while true 循环，
    while 1==1:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp -my_power
        # 如果我的血量小于0且我的血量大于敌人的血量，是我赢了。
        if my_hp <=0 and my_hp>enemy_hp:
            print(f"我赢了，我的血量是{my_hp},敌人的血量是{enemy_hp}")
            break
        # 如果我的血量小于0且我的血量小于敌人的血量，是我输了。
        elif my_hp <=0 and my_hp<=enemy_hp:
            print(f"我输了，我的血量是{my_hp},敌人的血量是{enemy_hp}")
            break
#利用列表推导式生成hp,
# if __name__ == '__main__':
#利用for循环生成随数。
hp = [x for x in range(900, 1010)]
enemy_hp=random.choice(hp)
print("敌人的总血量"+str(enemy_hp))
enemy_power = random.randint(190, 210)
print("敌人的攻击力"+str(enemy_power))
fight(enemy_hp,enemy_power)