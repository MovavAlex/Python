# #список - []
# #кортеж - ()
# #множества - {}
# #словарь - {"key": value}
#

# def hellow_orld(): #обьявляем функцию
#     print("Hello_World")
#
#
# hellow_orld() # вызов функции
#
#
# def plus(num1,num2):
#     result = num1+num2
#     print(result)
# plus(5,3)# вызов функции с аргументом, результат записан в переменную
# plus(num1=2, num2=2) # указывание конкретных аргументов
#
# a = input("Имя: ")
#
# def is_anton(name):
#     if name == "Антон":
#         return  True
#
#
# if is_anton(a):
#     print("Это Антон")
# else:
#     print("Это не Антон")
#

#Задача3

#
# def find_longest(list):
#     spisok2 = []
#     for i in list:
#         spisok2.append(len(i))
#     maxy = max(spisok2)
#     ind = spisok2.index(maxy)
#     return list[ind],spisok2[ind]
# spisok = ["Бараны", "Дом", "Дед", "Диван","Танго"]
#
# print(find_longest(spisok))

#Задача 4

# def min_max(lst):
#     maxi = lst[0]
#     mini = lst[0]
#     for i in lst:
#         if maxi > i:
#             maxi = i
#         elif mini < i:
#             mini = i
#     return maxi, mini
# lst = [5, 1, 6, 3, 8, 7, 2, 9, 4]
# print(min_max(lst))

#Задача 5

# def is_prime(func):
#     for i in range(2,func+1):
#         if i == func:
#             return True
#         if func % i == 0:
#             break
#
#
# if is_prime(48721):
#     print("True")
# else:
#     print("None")

#Задача 6

# def join(spisok:list,separate:str)->str:
#     result = ""
#     for i in spisok:
#         result += i+separate
#     return result
# lst = ["Строка1", "Строка2", "Строка3"]
# print(join(lst,"|"))


# Задача 7

# def factorial(chislo):
#     x = 1
#     for i in range(2,chislo+1):
#         x *= i
#     return x
#
# print(factorial(7))