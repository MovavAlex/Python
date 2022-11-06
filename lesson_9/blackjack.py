print("Добро пожаловать в 'BlackJack'!")
import random
is_game = "y"
while is_game == "y":
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] #10,10,10 - король, дама, валет. 11 - туз
    hand_player = [random.choice(cards)]
    hand_computer = [random.choice(cards)]
    score_player = 0
    score_computer = 0
    get_card = "y"



    while get_card == "y":
        hand_player.append(random.choice(cards))

        #если туз u > 21
        if sum(hand_player) > 21 and 11 in hand_player:
            for i in range(0, len(hand_player)):
                if hand_player[i] == 11:
                    hand_player[i] = 1

        score_player = sum(hand_player)
        print(f"Твоя рука: {hand_player}. Очков: {score_player}")
        print("Первая карта компутера: ", hand_computer[0])
        if score_player > 21:
            get_card = "n"
        else:
            get_card = input("y - взять карту, n - остановиться")

        while sum(hand_computer) < 17:
            hand_computer.append(random.choice(cards))

            if sum(hand_computer) > 21 and 11 in hand_computer:
                for i in range(0, len(hand_computer)):
                    if hand_computer[i] == 11:
                        hand_computer[i] = 1

    score_computer = sum(hand_computer)
    print("=" * 10)
    print(f"Твоя итоговая рука: {hand_player}, Очков: {score_player}")
    print(f"Итоговая рука компьютера: {hand_computer}, Очков: {score_computer}")

    if score_computer > 21 and score_player > 21:
        print("Перелет у обоих, ничья!")
    elif score_player > 21:
        print("Твой перебор. Ты проиграл ;(")
    elif score_computer > 21:
        print("Перебор компьютера. Ты победил!")
    elif score_player > score_computer:
        print("Твоя победа!")
    elif score_computer > score_player:
        print("Победа компьютера")
    else:
        print("Ничья!")

is_game = input("Ну что? Играем дальше? y - да, n - нет")







