class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print(self):
        print('Кот\кошка: %s; пол: %s; возраст: %d.' % (self.name, self.gender, self.age))