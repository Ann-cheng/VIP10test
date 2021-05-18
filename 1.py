class Solder():
    def __init__(self,name):
        self.name = name

class Bullet():
    def __init__(self,num):
        self.num = num
    def shooting(self):
        self.num -= 1
        print(f'士兵{self.name}开枪了,现在子弹还有{self.num}')
    def add(self):
        self.num += 1
        print(f'士兵{self.name}添加了子弹,现在子弹还有{self.num}')
wuqi=Bullet("AK")
solder1=Solder('瑞恩')
wuqi.shooting()