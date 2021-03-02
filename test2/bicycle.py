# -*- coding: utf-8 -*-
class Bicycle :
    def run(self,lucheng):
        print(f"骑行了{lucheng}公里")

fei = Bicycle()
fei.run(25)

class EBicycle(Bicycle):
    def fly(self,lu):
        print(f"电车骑行了{lu}里")
ya=EBicycle()
ya.fly(26)
ya.run(68)