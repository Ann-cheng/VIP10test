# 实现步骤：
# 定义⽗类，并提供公共⽅法
# 定义⼦类，并重写⽗类⽅法
# 传递⼦类对象给调⽤者，可以看到不同⼦类执⾏效果不同
class Dog(object):
    def work(self):  # ⽗类提供统⼀的⽅法，哪怕是空⽅法
        print('指哪打哪')

class ArmyDog(Dog):# 继承Dog类
    def work(self): # ⼦类重写⽗类同名⽅法
        print('追击')

class DrugDog(Dog):# 继承Dog类
    def work(self):# ⼦类重写⽗类同名⽅法
        print('缉毒')

class Person(object):
    def work_with_dog(self,dog): # 传⼊不同的对象，执⾏不同的代码，即不同的work函数
        dog.work()

ad = ArmyDog()
dd = DrugDog()
daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
