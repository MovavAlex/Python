# f = open('Trtrtrtr.txt', 'w', encoding ="utf-8)")
#                                 # Создаст если нет, перезапишет, если есть
# f.write("x\n")
# f.write("n\n")
# f.write("m\n")
# f.write("y\n")
# f.write("i\n")
#
# f.close()

#
# w = open('Trtrtrtr.txt', 'r', encoding="utf-8")
# # content = w.read() #считываем содержимое файла и помещаем в content
# content = w.readlines()
# print(content)
# for logarifm in content:
#     print(logarifm, sep='\n')
# w.close()
#


#1 Задача

# c = input("Введите имя файла: ")
# print("Начинайте вводить строки: ")
# f = open(f"{c}", 'w', encoding='utf-8')
# for i in c:
#     p = input(">>>")
#     f.write(f'{p}\n')
#     if p == "":
#         break
# print("Ответ записан")
# f.close()

#
# g = 0
# c = input("Введите имя файла: ")
# print("Начинайте вводить строки: ")
# f = open(f"{c}", 'w', encoding='utf-8')
# while g == 0:
#     p = input(">>> ")
#     f.write(f'{p}\n')
#     if p == "":
#         g += 1
# print("Ответ записан")
# f.close()
#


# # 2 Задача
# c = input()
# f = open(c,'r')
# content = f.readlines()
# l = len(content)
# for i in range(l):
#     print(f"{i+1})", content[i].strip())
#
#


# Задача 3










# n = int(input())
# f = open("Trtrtrtr.txt", "r")
# text = f.readlines()
# for i in range(n):
#     print(text[i].strip())
# f.close()
#
#
# n = int(input())
# f = open("Trtrtrtr.txt", "r")
# text = f.readlines()
# for i in range(n):
#     print(text[-i-1].strip())
#
# f.close()
#


#
# num = int(input())
# f = open("Trtrtrtr.txt", 'r', encoding='utf-8')
# content = f.readlines()
# s = len(content)
# sum = s // num
# if s % num != 0:
#     sum += 1
# print(sum)
#
# for i in range(sum):
#     j = open(f"{i+1}.txt", 'w', encoding='utf-8')
#     x = content[:i]
#     for u in x:
#         j.write(u)
#     del content[:2]
#
#

# f.close()