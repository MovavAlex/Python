# import random
#
# life = 10
# length = 3
#
# answer = random.randint(100, 999)
# answer = str(answer)
#
# while life:  # пока жизни != 0
#     is_guessed = False
#     print("=" * 10)
#
#     print("Жизней: ", end="")
#     for _ in range(life):
#         print("♥", end="")
#     print()
# 8
#     guess = input("Предположение: ")
#     if len(guess) != length or not guess.isdigit():
#         print("Число от 100 до 999")
#         continue
#
#     if guess == answer:
#         print("Пабеда 🏆")
#         is_guessed = True
#         break
#
#     if is_guessed == False:
#         # проверка на fermi
#         for i in range(length):
#             if guess[i] == answer[i]:
#                 print("Fermi")
#                 is_guessed = True
#                 break
#
#     if is_guessed == False:
#         for char in guess:
#             if char in answer:
#                 print("Pico")
#                 is_guessed = True
#                 break
#
#     if is_guessed == False:
#         print("Bagels")
#
#     life = life - 1

import random
import datetime

while True:
    number = input("Сколько дней рождения генерим?")
    if not number.isdigit() or int(number) > 70 or int(number) < 2:
        print("Это по-твоему смешно? число от 2 до 70")
        print("=" * 10)
    else:
        number = int(number)
        break

birthdays = []
startOfYear = datetime.date(2022, 1, 1) #год месяц день

for _ in range(number):
    #cлучайный сдвиг
    shiftOfDays = datetime.timedelta(random.randint(0,364)) #случ. сдвиг дней
    birthday = startOfYear + shiftOfDays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}. {birthdays[index]}")

print("=" * 10)
for i in set(birthdays):
    if birthdays.count(1) > 1:
        print(f"= {i.strftime('%d.%m.%y')} встречается {birthdays.count(index)}")














