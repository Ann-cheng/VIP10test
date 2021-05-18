# 不带参数的__init__()
class Washer():
    # 定义初始化功能的函数
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 300
    def wash(self):
        print(f'洗衣机宽度是{self.width},高度是{self.height}')
work = Washer()
work.wash()


# 带参数的__init__()
class Washer2():
    # 定义初始化函数
    def __init__(self,width,height):
        self.a = width
        self.b = height
    def wash2(self):
        print(f'洗衣机的宽度是{self.a},高度是{self.b}')
work2 = Washer2(30,40)
work2.wash2()


# str方法
class Washer3():
    def __init__(self,width,height):
        self.a = width
        self.b = height
    def __str__(self):
        return '这是海尔说明书'
work3 = Washer3(60,70)
print(work3)


# del方法