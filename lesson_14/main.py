# Множества
# 1 Повторения исключены
# 2 Неупорядоченные
# 3 Пустое множество - только set()
# 4 Внутри только неизменяемые данные


# Словари
# 1 Изменяемый тип данных
# 2 В качестве ключа допускается любое значение


# x = ("Что то")
# d = {
#     True: 1,
# }
# print(d)

# 3 Пустой словарь - dict() или {}



# Первая задача.

# symbols = list("?!,.")
# d = {}
# phrase = "Маша, ты где? Маша загорает.".lower() #Опустили регистр
# phrase_clear = ""
# for letters in phrase:
#     if letters not in symbols:
#         phrase_clear += letters
# print(phrase_clear)
# print("-----------------------------")
# l = phrase_clear.split(" ")
# for bogdan in l:
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)
#
#

# Вторая задача

# s = 0
# d = {"Хлеб": 1000,
#      "Молоко": 1.5,
#      "Сырок": 47,
#      "Елка": 50,
#      }
# # for price in d: #перебор по ключам
# for price in d.values(): #перебор по значениям
#     s += price
#
# print("Сумма:", s)



# Третья задача

# symbols = list("?!,.")
# d = {}
# phrase = "Маша, ты где? Маша загорает.".lower() #Опустили регистр
# phrase_clear = ""
# for letters in phrase:
#     if letters not in symbols:
#         phrase_clear += letters
#
# l = phrase_clear.split(" ")
# for bogdan in l:
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
#
#
# maxi = max(d.values())
# for k,v in d.items():
#     if v == maxi:
#         print(f"Наибольшее число повторений: {k}, Значение: {v}")

# Четвертая задача


d = {
    "Ключ1": 1,
    "Ключ2": 2,
    "Ключ3": 3,
    "Ключ4": 4,
    "Ключ5": 5,
    "Ключ6": 6,
    "Ключ7": 7
}
d["Ключ7"]
d["Ключ1"]

d["Ключ7"], d["Ключ1"] = d["Ключ1"], d["Ключ7"]
print(d)
new_d = {}
print("-------------------------------------------------------------------------------------------------")
del d["Ключ6"]
print(d)














# one = 1
# two = 2

# # three = 0
# #
# # three += one
# # one = 0
# # one += two
# # two = 0
# # two += three
#
# # one,two = two,one
# # print(one,two)


















# x = 1000
#
# while x > 0:
#     x -= 7
#     print(x)
