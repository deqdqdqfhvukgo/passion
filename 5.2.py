class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def work(self):
        print(f'{self.name}在工作')

class Teacher(People):
    def __init__(self, name, age, gender, salary, tel):
        super().__init__(name, age, gender)
        self.salary = salary
        self.tel = tel

    def work(self):
        print(f'{self.name}在授课')

    def play(self, sport):
        print(f'{self.name}正在进行{sport}')

# 测试代码
t = Teacher('汤姆', 23, '男', 6666, '1754635343')
t.work()
t.play('捉老鼠')
