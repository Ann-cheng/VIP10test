class Washer():
    def wash(self):
        print('我会洗衣服')
        print(self)
        # 类里面获取
        print(f'洗衣机的跨度是{self.weight},洗衣机的高度是{self.height}')
        # 类外面获取
        print(f'洗衣机的跨度是{help1.weight},洗衣机的高度是{help1.height}')

help1=Washer()
help1.weight=500
help1.height=300
help1.wash()
