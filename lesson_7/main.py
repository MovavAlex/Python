#ZeroDivisionError
#print(55/0)
#TypeError
#x = 1 + "один"

# lst = ["один", 2, "Антон"]
# lst = [3]

#SyntaxError
#if 5 < 0


#exit code:
# 0 - все хорошо
# 1 - ошибка
# =1 - прерывание

#NameError
#print(x)

#try: #попытаться
 #   number = int(input("введи число: "))
  # x = 5 / number
  #  print(x)

# except ZeroDivisionError: #ловим исключения
#     print("На ноль делить низя")
# except ValueError: # если вводят буквы
#     print("Хачу цифирку")
# except Exception: #обработка любой ошибки
#     print("Одна ошибка и ты ошибся")

#try:
   # name = input("Введите имя: ")
 #   if name == "Антон":
    #    raise Exception("Это имя запрещено!")
#except Exception as error_m: #складываем исключение в error_m
  #  print("Я запрещаю вам!", error_m)
#else: #иначе, если не вызвалися исключения
 #   print("Ну вот такое имя можна")
#finally:   #сработает в любом случае
 #   print("Я отработал")

# try:
#     number =  int(input("Введите число"))
#     x = 5 / number
# except Exception:
#     pass #затычка, заглушка
#
# if 3 == 3:
#     pass # ToDO: не забудь дописать и купить молока

#temperature = 365  # я комментарий
#print()

def summa(numbers): #def - обьявить функцию
    return sum(numbers) #возвращаем сумму чисел
print(summa([1,2,3])) # печатаем рез-т функцию при [1,2,3]
#assert
