class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def work(self):
        print(f'{self.name}在工作')

# 测试代码
p = Person('汤姆', 23, '男')
p.work()
