class Master(object):
    def __init__(self):
        self.kongfu = '[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[香辣煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(School, Master):
    pass
xiaoming = Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()