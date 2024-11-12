class Car:
    warning = "喝酒不开车，开车不喝酒!"

    def __init__(self, cno, brand, price, color):
        self.cno = cno
        self.brand = brand
        self.price = price
        self.color = color

    def print_info(self):
        print(f'车牌{self.cno}是{self.brand}，价格{self.price}元，颜色为{self.color}')

    def drive(self, dest):
        print(Car.warning)
        print(f'{self.cno}开往{dest}')

    @classmethod
    def set_warning(cls, new_warning):
        cls.warning = new_warning

if __name__ == '__main__':
    c = Car('京A12345', 'Toyota', 200000, '红色')
    c.print_info()
    Car.set_warning("安全驾驶，远离危险!")
    c.drive('海南岛')
