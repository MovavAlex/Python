# # # def hello(x):
# # #     return "Hello " + x + "!"
# # # x = input("Введите имя: ")
# # # print(hello(x))
# # #
# # # l = lambda x,b: "hello " + b + x #обьявление лямбда функции
# # # print(l("Антон ", "Jolyne"))# вызов лямбда функции
# # #
# # #
# # #
# #
# #
# # # генератор списка(list comprehension)
# #
# # lst = [i for i in range(1,6)]
# # print(lst)
#
#
# from random import randint
# #
# # fasolini = 20
# # player_1 = 0
# # player_2 = 0
# #
# #
# #
# #
# #
# # while fasolini
# # while True:
# #     print("Ход первого игрока")
# #     a = int(input("1, 2 или 3: "))
# #     fasolini -= a
# #     player_1 += 1
# #     try_play = 1
# #     print(f"Осталось {fasolini} бобов")
# #
# #     print("-----------------------------")
# #
# #     print("Ход второго игрока")
# #     b = int(input("1, 2 или 3: "))
# #     fasolini -= b
# #     player_2 += 1
# #     print(f"Осталось {fasolini} бобов")
# #     print(f"1 игрок {player_1}, 2 игрок {player_2}")
# #
# #     print("-----------------------------")
# #
# #     if fasolini == 1:
# #         break
# #
# #
# #
# #
# #
# # if player_1 > player_2:
# #     print("========== ПОБЕДИЛ ВТОРОЙ ИГРОК ==========")
# # else:
# #     print("========== ПОБЕДИЛ ПЕРВЫЙ ИГРОК ==========")
# #
# #
#
#
#
#
#
# fassol = 20
#
#
# def beans(x:int):
#     global fassol
#     fassol -= x
#
#
# while True:
#     first = int(input("2 игрок, 1, 2 или 3 фасоли? "))
#     if first <= 3 and first >= 1:
#         break
#     beans(first)
#     if fassol < 1:
#         print("Первый вин")
#         break
#     elif fassol == 1:
#         print("Первый вин")
#     else:
#         print(f"Фасоли: {fassol}")
# while True:
#     second = int(input("2 игрок, 1, 2 или 3 фасоли? "))
#     if second <= 3 and second >= 1:
#         break
#     beans(second)
#     if fassol < 1:
#         print("Второй вин")
#         break
#     elif fassol == 1:
#         print("Второй вин")
#     else:
#         print(f"Фасоли: {fassol}")
#
#


from random import randint

a = int(input("Введите сколько костей бросаем: "))
maximum = a*6
slovar = {}

for i in range(a, maximum+1):
    slovar[i] = 0

print(slovar)


