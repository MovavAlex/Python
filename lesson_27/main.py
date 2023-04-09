
#
# x = 14
#
# if type(x) == int:
#     a = x
# elif type(x) == float:
#     a = x + 1
#
# print(int(a))



# a = 1010
# b = 1011
# z = bin(a)[2:]
# n = bin(b)[2:]
# i = int(z+n)
# print()











# colors = ('желтый','красный','синий')
#
# color1 = input('Введите первый цвет:  ').lower()
# color2 = input('Введите второй цвет:  ').lower()
#
# if color1 in colors and color2 in colors:
#     if color1 == 'желтый' and color2 == 'красный' or color1 == 'красный' and color2 =='желтый':
#         print('Оранжевый')
#     elif color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 =='красный':
#         print('Фиолетовый')
#     elif color1 == 'синий' and color2 == 'желтый' or color1 == 'желтый' and color2 =='синий':
#         print('Зелёный')
# elif color1 not in colors or color2 not in colors:
#     print('Один из основных цветов введён неверно!')







colors = ('желтый','красный','синий')

# color1 = input('Введите первый цвет:  ').lower()
# color2 = input('Введите второй цвет:  ').lower()
#
# if color1 in colors and color2 in colors:
#     if (color1 == colors[0] and color2 == colors[1]) or (color1 == colors[1] and color2 ==colors[0]):
#         print('Оранжевый')
#     elif (color1 == colors[1] and color2 == colors[2]) or (color1 == colors[2] and color2 ==colors[1]):
#         print('Фиолетовый')
#     elif (color1 == colors[2] and color2 == colors[0]) or (color1 == colors[0] and color2 ==colors[2]):
#         print('Зелёный')
# elif color1 not in colors or color2 not in colors:
#     print('Один из основных цветов введён неверно!')














# colors = ('желтый', 'красный', 'синий')
#
# color1 = input('Введите первый цвет:  ').lower().strip()
# color2 = input('Введите второй цвет:  ').lower().strip()
# one = ''
# two = ''
# if color1 in colors and color2 in colors:
#     for i in colors:
#         if i == color1:
#             one += i
#         elif i == color2:
#             two += i
#
#         if one ==  and two == 'красный' or one == 'красный' and two == 'желтый':
#             print('Оранжевый')
#             break
#         elif one == 'красный' and two == 'синий' or one == 'синий' and two =='красный':
#             print('Фиолетовый')
#             break
#         elif one == 'синий' and two == 'желтый' or one == 'желтый' and two =='синий':
#             print('Зелёный')
#             break
#
# elif color1 not in colors or color2 not in colors:
#     print('Один из основных цветов введён неверно!')
















# start = input('Начало первого урока (чч:мм): ')
# log = int(input('Длительность урока (мин): '))
# perem = int(input('Длительность перемен (мин): '))
# count = int(input('На сколько уроков нужно расписание: '))
# a = start.split(':')
# hours = int(a[0])
# minutes = int(a[1])
# time = hours*60 + minutes
# for i in range(1, count+1):
#     print(f'{i} урок: ', end='')
#     print(f'{str(hours).rjust(2,"0")}:{str(minutes).rjust(2,"0")} - ', end='')
#     time += log
#     hours = time // 60
#     minutes = time % 60
#     print(f'{str(hours).rjust(2,"0")}:{str(minutes).rjust(2,"0")}')






# zomb = int(input('Сколько зомби было к началу расчёта: '))
# possib = int(input('Сколько каждый может заразить: '))
# days = int(input('На который день делаем расчёт: '))
# print(f'1 день: {zomb}')
# for i in range(2, days+1):
#     zomb = (zomb + zomb) * possib
#     print(f'{i} день: {zomb}')








# a = [1, 3, 5, 6, 10]
# for i in range(len(a)+1):
#     print(i)
#     try:
#         result = a[i + 1] + a[i - 1]
#     except IndexError:
#         if a[i+1] == IndexError:
#             result = a[i-1]+1
#         elif a[i-1] == IndexError:
#             result = a[i+1]+1
#     print(result)








#>>> Начало первого урока (чч:мм): 08:00
# >>> Длительность урока (мин): 45
# >>> Длительность перемен (мин): 10
# >>> На сколько уроков нужно расписание: 4
# 1 урок: 08:00 - 08:45
# 2 урок: 08:55 - 09:40
# 3 урок: 09:50 - 10:35
# 4 урок: 10:45 - 11:30


 # m += log
    # p = m + perem
    #
    # if m >= 60:
    #     n += 1
    #     m -= 60
    #
    # if p >= 60:
    #     l += 1
    #     p -= 60
    #
    # if n < 10:
    #     g = f'0{n}'
    #
    # if l < 10:
    #     o = f'0{l}'
    #
    # nach = f"{o}:{p}"
    #
    # result = f'{g}:{m}'
    # print(f'{i} урок: {nach} - {result}')







