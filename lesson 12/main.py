#списки
# lst = ["один", "два", "три"]
#lst.append("четыре")# - добавить элемент в список
#lst.pop(2) - убирает# - элемент из списка по индексу
#lst.remove("два") #- убирает элемент по значению

# lst = [0,3,5,-2,1]
# lst.reverse() # перевернуть порядок элементов в списке
# print(lst)

# lst1 = [0,1,2]
# lst2 = [3,4,5]
#
# lst1.extend(lst2) # обьединяет список путем расширения первого спика за счет второго
#
#
#
# print(lst1)


# lst = [1,2] # [1.2] = [1,1.5,2]
#
# lst.insert(1, 1.5) # вставить по индексу


# lst = ["не пустота"]
# lst.clear() # очистить список
# print(lst)


# lst = [0,4,2,-5,1]
#
# lst.sort() # отсортировать от меньшего к большему числу
# lst.sort(reverse=True) # отсортировать от большего к меньшему числу
# print(lst)
#
# # кортеж
# tup = (1,2,3)
# tup = 1, 2, 3
# rup = 1
# print(max(tup))
# print(min(tup))

# list1 = ["A","B","C"]
# list2 = ["0","1","2"]
# couple = zip(list1, list2)
#
#
# for bogdan in couple:
#    print(bogdan)

# from collections import namedtuple
#
# citizen = namedtuple("Житель", "имя возраст статус какую_группу_уважаешь")
# alex = citizen(имя="Леха Алексеев",
#                возраст="27",
#                статус="Предприниматель",
#                какую_группу_уважаешь="Аллу Пугачеву")
#
# print(alex.имя)
# print(alex.какую_группу_уважаешь)
# print(alex.статус)
#
# print(alex)