# import random
# primer1 = lambda a,b: a + b + 1 # лямбда функцию поместили в переменную
#
# print(primer1(5,10))

# answer = str(input("Введите букаву: "))
#
# exit_trigger = lambda yn: True if yn == "Д" else False
# print(exit_trigger(answer))


#генератор списка (list comprehension)

# lst = []
#
# for i in range(1,6):
#     lst.append(i)
# print(lst)
#
#
# c2f = lambda c : 9/5 * c + 32
# f2c = lambda f : (f - 32) * 5/9
# c2k = lambda c : 273.15 + c
# k2c = lambda k : k - 273.15
# f2k = lambda f : c2k(f2c(f))
# degree = 203
# print(c2k(degree))


# exit = lambda yn: True if yn == "Д" else False
# while True:
#     num = int(input("Сколько бросаем кубов?"))
#     dices = [random.randint(1,6) for i in range(num)]
#     print(dices)
#
#     a = input("Бросаем еще? Н/Д")
#     if exit(a) == True:
#         continue
#     else:
#         break

# from random import choice
# site = input("Введите ссылку: ")
#
# lst = [list("ABCDEFGHIjKLMNOPQRSTUVWXYZ"),
#        list("abcdefghijklmnopqrstuvwxyz"),
#        list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#        list("абвгдеёжхзийклмнопрстуфхцчшщъыьэюя"),
#        list("1234567890")]
#
# bukvi1 = []
#
# for i in range(6):
#     bukvi1.append(choice(choice(lst))) #случайный список
#
# code = "".join(bukvi1)
#
# dictionary = {}
# print(f">>> {site}\nСсылка сокращена. Ваш код: {code}")
# print("-------------------------------------------------------------")
# print(dictionary)
#
# if site in dictionary:
#     print(f"Ссылка уже сокращалась, вот её код: {dictionary[site]}")
# else:
#     dictionary[site] = code
#     print(f"Ссылка добавлена. Вот её код: {code}")
import math
print("")
print("                                                                         Решите задачи:")
print("")
print("                                                                           x + a = b\n"
      "                                                                           x - a = b\n"
      "                                                                           x * a = b\n"
      "                                                                           x / a = b\n"
      "                                                                           a / x = b\n"
      "                                                                           |x| = b\n"
      "                                                                           a**x = b")
print("")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
a = int(input("a:"))
b = int(input("b:"))
x = int(input("x:"))

ques1 = lambda a, b: b-a
ques2 = lambda a, b: b+a
ques3 = lambda a, b: b/a
ques4 = lambda a, b: b*a
ques5 = lambda a, b: a/b
ques6 = lambda x: -x if x<0 else x




print(
    "x = ", ques1(a,b),"\n"
    "x = ", ques2(a,b), "\n"
    "x = ", ques3(a,b),"\n"
    "x = ", ques4(a,b),"\n"
    "x = ", ques5(a,b),"\n"
    "x = ", ques6(x)
      )

# logarifm = lambda a,b: math.log(b, a)
# print(math.log())
#




