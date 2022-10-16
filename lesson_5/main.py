# x = int(input("число."))
#
# if x >= 10:
#     print("Я сработал")
# if x <= 10:
#     print("Ну я тоже сработал") #больше или равно либо меньше или равно
#
# phrase = "Я карта"
# if phrase =="ya karta":
#     print("Мы в мире настоящих мужчин") #равность
#
# game = "dota2"
# if game != "brawl stars":
#     print("можно поиграть") #проверка не равность

#
# if x >= 10 and x == 0 or x == 666:
#     print("Я не выполнюсь, хоть и ошибок нет")
# else:
#     print("Ну я тоже сработав")
#
# if x >= 10 and (x == 0 or x == 666):
#     print("Я не выполнюсь, хоть и ошибок нет")
# else:
#     print("Ну я тоже сработав")


# number = int(input("Введи число:"))
# if number > 0:
#     print("Положительное")
# elif number == 0: #elif = else if (иначе если)
#     print("Ноль")
# else:
#     print("Отрицательное")



#year = int(input("Введи год: "))
#if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)  :
  #  print("Високосный год")
#else:
 #   print("Не високосный год")


#numb_1 = int(input("Первое число"))
#operation = input("Введи операцию(-,+.*./):").strip() #ввод операции
#numb_2 = int(input("Второе число"))
#lst = ["-","+","*","/"] #список допустимых операций

#if operation in lst:
 #   if operation == "-":
  #      print(numb_1 - numb_2)
   # elif operation == "+":
   #     print(numb_1 + numb_2)
   # elif operation == "*":
   #     print(numb_1 * numb_2)
   # elif operation == "/":
     #   print(numb_1 / numb_2)


# numb_1 = int(input("Первое число"))
# numb_2 = int(input("Второе число"))
# numb_3 = int(input("Третье число"))
#
# counter_pol = 1 #положительные
# counter_otr = 0 #отрицательные
#
# if numb_1 < 0:
#     counter_otr += 1 #прибавить к отрицательным
# else:
#     counter_pol += 1
#
# if numb_2 < 0:
#     counter_otr += 1  # прибавить к отрицательным
# else:
#     counter_pol += 1
#
# if numb_3 < 0:
#    counter_otr += 1  # прибавить к отрицательным
# else:
#     counter_pol += 1
#
# print("Положительных:", counter_pol)
# print("Отрицательных:", counter_otr)
#

# numb_1 = int(input("Первое число"))
# numb_2 = int(input("Второе число"))
# numb_3 = int(input("Третье число"))
#
# lst = [numb_1, numb_2, numb_3]
#
# maxi = max(lst)
# mini = min(lst)
# print("Минимальное:", mini)
# print("Максимальное:", maxi)




ticket = input("номер билета")
if len(ticket) == 6 and ticket.isdigit():
    first_half = ticket[:3]
    last_half = ticket[-3:]

    first_sum = first_half[0] + first_half[1]+ first_half[2]
    last_sum = last_half[0]+ last_half[1]+ last_half[2]

    if first_sum == last_sum:
        print("счастливый билет")
    else:
        print("Не повезло")
else:
    print("Введи нормально, пожалуйста: ")


