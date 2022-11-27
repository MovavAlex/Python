import os


total_bets = []
trigger = "yes"

while trigger == "yes":
    name = str(input("Введите имя:"))
    bet = int(input("Ваша стаака:"))
    temp_bet = {"nsme": name, "bet": bet}
    total_bets.append(temp_bet)
    trigger = input("yes - продолжаем, no - останавливаем(")
    os.system("cls||clear")

winner = {"name": '', "bet": 0}
for i in range(len(total_bets)):
    if total_bets[i]["bet"] > winner["bet"]:
        winner["name"] = total_bets[i]["name"]
        winner["bet"] = total_bets[i]["bet"]

print(f"Победитель: {winner['name']}. Его ставка: {winner['bet']}")