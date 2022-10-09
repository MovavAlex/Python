# print("введи стоимость пирожка")
# rub =int(input("Рубли: "))
# cop =int(input("Копейки: "))
# n = int(input("Кол-во пирожков: "))
#
# price_pie = ru#b * 100 + cop
# need_to_pay = price_pie * n
# print(f"С вас {need_to_pay // 100} рублей и {need_to_pay % 100} копеек")
#
# money = int(input("Рублев в кармане: "))
# sdacha = money * 100 - need_to_pay
# print(f"ваша сдача {sdacha // 100} рублей и {sdacha % 100} копеек")
#
# a = int(input("a: "))
# if a % 2 == 1 :
#     a = a + 1
# else:
#     a = a + 2
#     print(a)
#
# r = int(input("Рад. окружности:"))
# print(3.14 * r ** 2)
#
# n = int(input("Секунды: "))
# hours = n // 3600
# minutes = n // 60
# if minutes >= n // 60:
#     hours = hours + 1
#     minutes = minutes - 60
# seconds = n % 60
# if hours < 10:
#     hours = "0" + str(hours)
#     if minutes < 10:
#         minutes = "0" + str(minutes)
# print(f"Время {hours}:{minutes}:{seconds}")

# x = '''Строка'''
# '''Строка 1 '''
# '''Строка
# x = "Что то"
# x = 'Что то'
# print("И он сказал: точка-точка-точка")

#x = ["А","Б","В","Г","Д","Е","Ё","Ж"]
#print('Строка:', x)
#print("Первый элемент = ", x[0])
#print("Последний элемент = ", x[-1])
#print("Первые 5 элементов через 1-ого: = ", x[0:5:2])
#print("Первые 5 элементов : = ", x[0:5])

#x = "Я строка, я карта, я Антон"
#print(x[-5:])
#print(x[:8])




#x = "Программирование"
#temp = x[-1]
#index = x.index(temp)
#print(index + 1)
#print(len(x))

#path = "C:/Python3/python.exe"
#print("Имя файла:", path[-10:])
#print("Расширение:", path[-3:])
#print("Имя каталога:", path[3:9])
#print("Полный путь к каталогу:", path[0:9])

#path2 = path.split("/")
#print(path2)


#print("Имя файла:", path2[-1])
#print("Расширение:", path2[-1][-3:])
#print("Имя каталога:", path2[1])
#print(f"Полный путь к каталогу:, {path2[0]}/{path2[1]}")


#charpter1 = input("Глава 1 - ")
#page1 =input("Страница 1 - ")

#charpter2 = input("Глава 2 - ")
#page2 =input("Страница  - ")

#charpter3 = input("Глава 3 - ")
#page3 =input("Страница  - ")


#print(charpter1.ljust(15), page1.rjust(15))
#print(charpter2.ljust(15), page2.rjust(15))
#print(charpter3.ljust(15), page3.rjust(15))

str = "12'345'678"
#temp = str.split("'")
#print(temp)
#number = int(temp[0] + temp[1] + temp[2])
#print(number)

## Решение через []
# temp = str[0;2] + str[3;6] + x[-3:]
# number = int(temp)
# print(number)

# решение через replace
temp = x.replace("'", "")
print(temp)