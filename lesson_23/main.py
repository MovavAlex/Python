import random
#import json
# # l = open('file.json', 'w', encoding='utf-8')
# # json.dump('Привет', l, ensure_ascii=False)
# # l.close()
# #
# # l = open('file.json', 'r', encoding='utf-8')
# # c = json.load()
# #
# class Person:
#     def __init__(self, imya, ages): #магический метод (инициализации)
#         self.name = imya
#         self.age = ages
#     def __str__(self):
#         return f'Я {self.name} и мне {self.age} лет'
#
#
# chelovek = Person(input('Введите имя '), int(input('Введите возраст '))) #создание обьекта класса Person
# chelovek1 = Person(input('Введите имя '), int(input('Введите возраст ')))
# print(chelovek.name, chelovek.age)
# print(chelovek1.name, chelovek1.age)
# print(str(chelovek))
#
#
#
#
# def mult(a, b):
#     return a*b
# a = int(input())
# b = int(input())
# print(mult(a, b))

# lst = []
# for i in range(random.randint(5,10)):
#     lst.append(random.randint(2,5))
# print(lst)

class fullname:
    def __init__(self, name, surname, age): #магический метод (инициализации)
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
        self.srba = sum(self.grades)/len(self.grades)



    def __str__(self):
        return f'Возраст: {self.age}\nИмя: {self.name}\nФамилия: {self.surname}'
    def greet(self):
        return f"Меня зовут {self.surname} {self.name}, мне {self.age}"


chelovek = fullname('Антон', 'Бананов', 21) #создание обьекта класса Person
chelovek1 = fullname('Володя', 'Антонов', 23)
print(f'Оценки:{chelovek.grades}\nСредний балл:{chelovek.srba}')
# print(chelovek.name, chelovek.surname, chelovek.age, chelovek.grades)
# print(str(chelovek))
# print(chelovek.greet())
#






