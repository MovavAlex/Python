# slovar = {"key1": "value1",
#           "key2": "value2",
#           "key3": "value3",
#           "key4": "value4",
#           "key5": "value5"}

# keys = []
# values = []
#
# #Решение циклом
# for i in slovar:
#     keys.append(i)
#     values.append(slovar[i])
# print(keys)
# print(values)



# #Решение без цикла
# keys = list(slovar.keys())
# value = list(slovar.values())
# print(keys)
# print(value)

###########################

# x = ["Никита", "Екатерина", "Андрей", "Андрей", "Анастасия", "Арсалан",
#      "Наталья", "Тимур", "Григорий", "Евгений", "Анастасия",  "Екатерина",
#      "Андрей", "Евгения", "Анастасия", "Герман", "Тимур", "Григорий",
#      "Арсалан", "Ярослава", "Есения", "Даниил", "Данил", "Андрей", "Никита"]
# a = input().capitalize()
# count = 0

## Решение циклом
#
# for i in x:
#     if a == i:
#         count += 1
# print(count)


##Решение без цикла

# print(x.count(a))


# a = float(input())
# print(round(a))

# from string import ascii_uppercase
# from random import choice
#
# alph = ascii_uppercase
# stri = ''
#
# n = int(input())
#
# for i in range(n):
#     stri += choice(alph)
#
# print(stri)
#
# s = set(stri)
# new_str = ''
# z = list(s)
#
# for i in range(len(z)):
#     new_str += z[i]
# print(new_str)



#
# while True:
#     a = input()
#     lst = a.split()
#     if 'суета' in lst[0].lower():
#         break


# x = "abcdefghijklmnopqrstuvw"
#
# new = ''
#
# for i in range(len(x)):
#
#     if i % 2 == 0:
#
#         new += x[i]
#
#
# rev = reversed(new)
#
# n = ''
#
# for i in rev:
#     n += i
#
# print(n)





# from random import randint
# s = set()
#
# for i in range(10):
#     s.add(randint(0, 15))
#
#
# sort = sorted(s, reverse=True)
#
# print(sort)





