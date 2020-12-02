def fight():
    #定义4个变量
    my_hp = 1000
    my_power =200
    enemy_hp = 1000
    enemy_power = 200
    #最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power
    #判断输赢
    #三目运算
    #print("我赢了") if my_final_hp>enemy_final_hp else print("我输了")
    # if my_final_hp>enemy_final_hp:
    #      print("我赢了"+str(my_final_hp)+" "+str(enemy_final_hp))
    # elif my_final_hp<enemy_final_hp:
    #     print("我输了"+str(my_final_hp)+" "+str(enemy_final_hp))
    # else :
    #      print("我输了"+str(my_final_hp)+" "+str(enemy_final_hp))
    print(f"我太冷了{my_final_hp}")
fight()
