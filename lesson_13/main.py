# a = [1, "qwerty", 2.5]
# b = set(a)
# c = len(b)
# print(c)



# a = {1, 2, 3, 4}
# b = {7, 2, 3, 8}
#
# y = a | b
# c = a & b
# i = a - b
#
#
# print(y, c, i)

#
# lst = [0,7,14,28,0,7]
# # 7 14 28 7
#
#
#
# for i in range(len(lst)):
#     if lst[i]>lst[i-1]:
#         print(lst[i], end=' ')
#
# print()
# for i in range(len(lst)):
#     if lst[i] < lst[i-1]:
#         print(lst[i], end=' ')
#
#
#
#

#
# lst1 = [3, 5, 6, 12, 54]
# lst2 = [54, 6, 251, 12]
#
# a = set(lst1)
# n = set(lst2)
# c = a & n
#
#
# b = sorted(c,reverse=False)
#
# print(b)
#
#



# lst = [1,2,4,2,6,1,2,9]
# count = []
# for i in range(len(lst)):
#     if lst[i] in count:
#         print("YES")
#     else:
#         count.append(lst[i])
#         print("NO")


#Дан список, найти наибольшее и наименьшее число без встроенных функций


# lst = [5,1,6,3,8,7,2,9,4]
#
# maximum = lst[0]
# minimum = lst[0]
#
# for i in lst:
#     if i > maximum:
#         maximum = i
#
#     if i < minimum:
#         minimum = i
#
# print("max: ", maximum)
# print("min: ", minimum)



#
# o ="...|                    |..."
# p ="...|                    |..."
# a ="...|                    |..."
# b ="...|                    |..."
# c ="...|                    |..."
# d ="...|                    |..."
# e ="....|                  |...."
# f ="....|                  |...."
# g ="....|                  |...."
# h ="....|                  |...."
# i ="....|                  |...."
# j =".....|                |....."
# k =".....|                |....."
# l =".....|                |....."
# m =".....|                |....."
# n ="......|______________|......"
#
#
# kahlua = "k"
# balleys = "b"
# cointreau = "c"
# fire = "!"
#
#
# fir = a.replace(" ","!")
# c1 = b.replace(" ", "c")
# c2 = c.replace(" ", "c")
# c3 = d.replace(" ", "c")
# b1 = e.replace(" ", "b")
# b2 = f.replace(" ", "b")
# b3 = g.replace(" ", "b")
# b4 = h.replace(" ", "b")
# b5 = i.replace(" ", "b")
# k1 = j.replace(" ", "k")
# k2 = k.replace(" ", "k")
# k3 = l.replace(" ", "k")
# k4 = m.replace(" ", "k")
#
#
# print()





# str(строка)
# int(целые числа)
# float(дробные числа)
# bool(буллевый тип данных)
# list(список "[]")
# set(множество "{}")
# tuple(кортеж "()")





# dict1 = {"Ключ1": 1,
#          "Ключ2": "Антон",
#          "Якрут": True,
#          "Словарь": {"Вл1": 1}
#          } #пример создания словаря
# empty_dictionary1 = {} # 1 способ создания пустого словарф
# empty_dictionary2 = dict()  # 2 способ создания пустого словарф
#
#
# print(dict1["Словарь"]["Вл1"])
#
#


# Циклы


# while и for
# x = 0
# b = 0
# while x != 5:
#     b += 1
#     print(b)
#     x += 1
# while True:
#     print(123)
# while False:
#     print(123)
#

# phrase = "фраза"
#
# # for supra in phrase:
# #     print(supra)

#
# for jojo in range(5):
#     print(jojo)
#
#


# empty_dict = dict() #единственный способ создания пустого множества
# set1 = {1,2,3}
# print(type(set1))

# set0 = {1,1,1,2}
# print(set0)
# set00 = {"A","B","Ц"}
# print(set00)
#
#
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
#
#
#
#
#
#
#
#
# print(set1.union(set2))
# print(set1 | set2)
#
# print(set1.intersection(set2))
# print(set1 & set2)
#
# print(set1.difference(set2))
# print(set1 - set2)
#
# #Симметрическая разность
#
# print(set1.symmetric_difference(set2))





from random import randint
#
# lst = []
# # count = 0
# # while count!=5:
# #     lst.append(randint(1,5))
# #     count += 1
#
# for i in range(5):
#     lst.append(randint(1,5))
#
# print(lst)
#
# lst1 = set(lst)
#
# print(f"Штук: {len(lst1)} {lst1}")
#
#




lst1 = []
lst2 = []
count = 0

for i in range(randint(100, 1000)):
    lst1.append(randint(0, 10000))
    lst2.append(randint(0, 10000))
    count += 1
set1 = set(lst1)
set2 = set(lst2)

a = set1 & set2
b = max(a)
c = min(a)
d = set1 | set2
d1 = list(d)
d1.sort()

print(f"Общих чисел: {len(a)}")
print(f"Кол-во генераций: {count}")
print(f"Максимальное значение: {b}")
print(f"Минимальное значение: {c}")
print(d1)