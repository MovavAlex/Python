# try:
#     f = open('file.txt', 'r', encoding='utf-8')
# except FileNotFoundError:
#     print("э")
#
#
#
#
#
# a = input("Что делаем? '/' -делим, '*' -умножаем, '+' - суммируем, '-'-минусуем ")
# x = int(input("Введи число: "))
# y = int(input("Введи второе число: "))
# if a == '/':
#     try:
#         print(f"Результат: {x/y}")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя")
# elif a == "*":
#     print(f"Результат: {x*y}")
# elif a == "-":
#     print(f"Результат: {x-y}")
# elif a == "+":
#     print(f"Результат: {x+y}")
#
#
#
# try:
#     x = int(input("Введи число: "))
#     print(10 / x)
# except ValueError:
#     print("Хочу число")
# except ZeroDivisionError:
#     print("На ноль нельзя")
# else:  # когда не было исключений
#     print("Молодец")
# finally:  # в любом случае исполняется
#     print('Конец')

# x = input("Введи имя друга: ").capitalize()
# try:
#     if x == 'Антон':
#         raise NameError("Антон вне закона")
# except NameError as a:
#     print("Нельзя!")
# def sr():
#     a = 0
#     k = 0
#
#     for i in content:
#         try:
#             a += int(i)
#         except ValueError:
#             print("Найдено не число", i)
#         else:
#             k += 1
#     if k == 0:
#         return "Чисел не найдено"
#     return round(a/k, 2)
#
# try:
#     f = open('file.txt', 'r', encoding='utf-8')
# except FileNotFoundError:
#     print("Файл не найден или написан неправильно")
#content = f.read().split()
#f.close()
#
# print(sr())

# try:
#     f = open('file.txt', 'r', encoding='utf-8')
# except FileNotFoundError:
#     print("Файл не найден или написан неправильно")
# text = f.readlines()
#
#
#
# s = ''.join(text).replace("\n", " ")
# words = ''.join(text).replace("\n", " ").split()
# sym = len(words)
# symbols = s.replace(' ', '')
# a = len(symbols)
# f.close()
# print(f'Строк: {len(text)}')
# print(f'Символов: {a}')
# print(f'Слов: {sym}')
#


# file = input("В каком файле будем искать?: ")
# word = input("Какое слово ищем?: ")
#
# try:
#     f = open(file, 'r', encoding='utf-8')
# except FileNotFoundError:
#     print("Файл не найден или написан неправильно")
# text = f.read()
# f.close()
# s = text.count(word)
# print(s)


# try:
#     f = open("file.txt", 'r', encoding='utf-8')
# except FileNotFoundError:
#     print("Файл не найден или написан неправильно")
# text = f.read()
# f.close()
#
# numbers = text.split()
# print(numbers)
# p = 0
# for i in numbers:
#     p *= int(i)
# print(p)