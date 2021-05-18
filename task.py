# 提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递，一定要先写逻辑分析，再写代码。
#
# 1、打印小猫爱吃鱼，小猫要喝水
class Cat():
    def work(self):
        print(f'小猫爱吃鱼,小猫要喝水')
cat = Cat()
cat.work()

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 4）小美的体重是45.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 类:person
# 属性:体重,名字
# 方法:跑步,吃东西
class Person():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def run(self):
        self.result_weight = self.weight-0.5
        print(f'{self.name}现在体重是{self.result_weight}')
    def eat(self):
        self.result_weight = self.weight+1
        print(f'{self.name}现在体重是{self.result_weight}')
xiaoming = Person('小明',75)
# xiaoming.run()
xiaoming.eat()


# 3、摆放家具
class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area
class House():
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.furniture=[]
    def __str__(self):
        return f'房子户型是{self.house_type},占地面积{self.area},剩余面积{self.free_area},里面的家具有{self.furniture}'
    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print(f'家具太大,无法容纳')
jia1 = House('大户型',30)

bed = Furniture('床',4)
jia1.add_furniture(bed)
# print(jia1)

wardrobe = Furniture('衣柜',2)
jia1.add_furniture(wardrobe)
# print(jia1)

table = Furniture("餐桌",1.5)
jia1.add_furniture(table)
print(jia1)
# 4.
# 士兵开枪
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

