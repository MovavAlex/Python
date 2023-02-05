from random import randint
import easygui

# # user_choose = easygui.msgbox(msg= "Hello World",
# #                              title="Усиленное приветствие",
# #                              ok_button="Понято",
# #                              image="img/бумага.png")
# # if user_choose == None:
# #     easygui.msgbox(msg="Ну пока")
# # elif user_choose == "Понято":
# #     print("ы")
#
#
# def rock_paper_scissors():
#     computer = randint(1,3)
#     user = easygui.buttonbox(msg="Выбери свой вариант",
#                              images=["img/камень.png", "img/ножницы.png", "img/бумага.png"])
#     if user == "img/камень.png" and computer == 2: # 1 2
#         easygui.msgbox(msg="Вы: Камень\n Компьютер: Ножницы. Вы выиграли!")
#     elif user == "img/ножницы.png" and computer == 1: # 2 1
#         easygui.msgbox(msg="Вы: Ножницы\n Компьютер: Камень. Вы проиграли!")
#     elif user == "img/ножницы.png"and computer == 3: # 2 3
#         easygui.msgbox(msg="Вы: Ножницы\n Компьютер: Бумага. Вы выиграли!")
#     elif user == "img/бумага.png" and computer == 2: # 3 2
#         easygui.msgbox(msg="Вы: Бумага\n Компьютер: Ножницы. Вы проиграли!")
#     elif user == "img/бумага.png" and computer == 1:  # 3 1
#         easygui.msgbox(msg="Вы: Бумага\n Компьютер: Камень. Вы выиграли!")
#     elif user == "img/камень.png" and computer == 3: # 1 3
#         easygui.msgbox(msg="Вы: Камень\n Компьютер: Бумага. Вы проиграли!")
#     elif user == "img/камень.png" and computer == 1:
#         easygui.msgbox(msg="Вы: Камень\n Компьютер: Камень. Ничья!")
#     elif user == "img/ножницы.png" and computer == 2:
#         easygui.msgbox(msg="Вы: Ножницы\n Компьютер: Ножницы. Ничья!")
#     elif user == "img/бумага.png" and computer == 3:
#         easygui.msgbox(msg="Вы: Бумага\n Компьютер: Бумага. Ничья!")
#
#
# def guess_the_number():
#     user_try = 7
#     computer_choice = randint(1, 100)
#     a = easygui.integerbox(msg="Отгадай число!")
#     while user_try != 0:
#         if a > computer_choice:
#             a = easygui.integerbox(msg=f"Нет, нужно меньше чем {a}",
#                                    image="img/меньше.png"
#                                    )
#             user_try -= 1
#         elif a < computer_choice:
#             a = easygui.integerbox(msg=f"Нет, нужно больше чем {a}",
#                                    image="img/больше.png"
#                                    )
#             user_try -= 1
#         elif a == computer_choice:
#             easygui.msgbox(msg=f"Поздравляю! Ты выиграл! Число было {a}")
#             break
#         if user_try == 0:
#             easygui.msgbox(msg=f"Упс! Кажется ты проиграл! :( Число было {computer_choice}")
#
#
#
# n = easygui.buttonbox(
#     msg="Выбери игру!",
#     title="Загадка",
#     choices=["Камень ножницы бумага", "Угадай число"]
#
# )
# if n == None:
#     easygui.msgbox(msg="Пака")
# elif n == "Камень ножницы бумага":
#     rock_paper_scissors()
# elif n == "Угадай число":
#     guess_the_number()

def training():
    power = 1
    agillity = 1
    intelligence = 1
    while True:
        user_try = easygui.buttonbox(msg=f"Сила: {power}\nЛовкость: {agillity}\nИнтеллект: {intelligence}",
                                     images=["img2/сила.png","img2/ловкость.png","img2/интеллект.png"],
                                     choices=["Покинуть тренировку"]
                                     )
        if user_try == "img2/сила.png":
            power += 1
        elif user_try == "img2/ловкость.png":
            agillity += 1
        elif user_try == "img2/интеллект.png":
            intelligence += 1

        if user_try == "Покинуть тренировку":
            return power, agillity, intelligence

m = training()
print(m)
def arena():
    ep = randint(1,5)
    ea = randint(1,5)
    ei = randint(1,5)
    easygui.buttonbox(msg=f"Статы врага:\nСила: {ep}\nЛовкость: {ea}\nИнтеллект: {ei}\n---------------------------------------------------------\nТвои статы:\nСила: {power}\nЛовкость: {agillity}\nИнтеллект: {intelligence}",
                              choices=["В бой!", "Отступить"])
    if ep < power and ea < agillity and ei < intelligence:
        easygui.msgbox(msg="Ура! Победа!")
    elif power < ep or agillity < ea and intelligence < ei:
        easygui.msgbox(msg="Поражение! Продолжай тренироваться и достигнешь небывалых высот!")





user1 = easygui.buttonbox(msg="Выбирай куда хочешь отправится",
                  choices=["Тренировка","Арена"]

)
if user1 == "Тренировка":
    training()
elif user1 == "Арена":
    arena()
elif user1 == None:
    easygui.msgbox(msg="До новых встреч")




























