
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

class Bullet():
    def __init__(self,name,num):
        self.name = name
        self.num = num
    def shooting(self):
            self.num -= 1
            print(f'士兵用{self.name}开枪了,现在子弹还有{self.num}')
    def add(self):
            self.num += 1
            print(f'士兵添加了子弹,现在子弹还有{self.num}')

wuqi=Bullet('ak',20)
wuqi.shooting()







