#month = input("Введите номер месяца:")
#if month.isdigit() and 1 <= int(month) <= 12:#.isdigit - число
 #   month = int(month)
  #  if 3 <= month <= 5:
#      print("Весна")
   # elif 6 <= month <= 8:
     #   print("Лето")
 #   elif 9 <= month <= 11:
       # print("Осень")
  #  else:
     #   print("Зима")
#else:
  #  print("Ты ошибся")

#h = int(input("Часы:"))
#m = int(input("минуты:"))
#s = int(input("секунды:"))

#if 23 >= h >= 0 and  59 >= m >= 0 and 59 >= s >= 0:
#    print("Формат правильный")
 #   print(f"{h}:{m}:{s}")
#else:
 #   print("ошибка")
  #  if h > 23 or h < 0:
  #      print("Часы в формате [0, 23]")
  #  elif m > 59 or m < 0:
   #     print("Минуты в формате [0.23]")
   # elif s > 59 or s < 0:
   #     print("Секунды в формате [0.23]")

count = 0
q1 = input("Какого цвета трава?\n"
           "a) Черная, б) Зеленая, г) Ответ А, в) перпл\n"
           "--> ")
if q1 == "б":
    print("Маладец")
    count = count+1
else:
    print("Не угадал")
    print("Твой счёт:", count)
    quit()

q2 = input("Сколько москво ситей в мире?\n"
            "a) адин, б) двести, в) многа, г) мала\n"
            "--> ")
if q2 == "а":
    print("Маладец")
    count = count+1
else:
    print("Не угадал")
    print("Твой счёт:", count)
    quit()
q3 = input("Туннель какой длины длинный?\n"
           "a) короткий, б) длинный, г) туннеля нет, в) очень длинный\n"
           "--> ")
if q3 == "в":
    print("Маладец")
    count = count+1
else:
    print("Не угадал")
    print("Твой счёт:", count)
    quit()

    print("Полная победа!")
