from player import MusicBox
pleer = MusicBox()
print('Для выхода введи пустую строку или "exit"')
while True == True:
    pleer.play()
    guess = input('Что ты услышал?')
    if guess == '' or guess == 'exit':
        break
    elif guess == 'венсдей':
        print('[Текст песни «ДЕВОЧКА УЭНСДЕЙ»]\n///\n[Интро]\nТы мне нравишься тем, что ни на кого не похожа\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа\n///\n[Припев]\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа\n///\n[Куплет 1]\nТы не улыбаешься, но веришь в любовь (Ты веришь в любовь)\nТак же как я (Между мной и тобой)\nЧто-то витает в нашей встрече, как второй сезон (Е-е)\nДумал не замечен, думал во френдзоне (У)\nОб друг друга разбиться, как она и я, она и я — это авария\n///\n[Припев]\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа\n[Куплет 2]\nНам так пофиг, чё там говорят за спиной (Пофиг, мне пофиг, мне пофиг)\nМы для них пришельцы, их учили выбирать любовь головой (Зачем головой?)\nОна с тобой сердцем, я помню первую встречу нашу, как будто бы вчера\nДа, пульс под двести, от своих песен я забыл слова\nКак мы разные, но так близки она и я, она и я, как аномалия\n///\n[Припев]\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа\nДевочка Уэнсдей с последней парты\nНапишу тебе песню, но не для топ-чарта\nДевочка Уэнсдей, грустный эмоджи\nТы мне нравишься тем, что ни на кого не похожа')
        pleer.wednesday()
    pleer.check(guess)

print(f'За игру у тебя набралось {pleer.get_score()} очка(ов)!')
