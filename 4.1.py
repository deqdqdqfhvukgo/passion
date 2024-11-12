class Car:
    def __init__(self, cno, brand, price, color):
        # 初始化汽车属性
        self.cno = cno
        self.brand = brand
        self.price = price
        self.color = color

    def print_info(self):
        # 打印汽车信息
        print(f'车牌{self.cno}是{self.brand}，价格{self.price}元，颜色为{self.color}')

    def drive(self, dest):
        # 打印目的地
        print(f'{self.cno}开往{dest}')

if __name__ == '__main__':
    c = Car('京A12345', 'Toyota', 200000, '红色')
    c.print_info()
    c.drive('海南岛')
