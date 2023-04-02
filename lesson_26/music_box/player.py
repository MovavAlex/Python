import playsound
from random import choice
class MusicBox:
    def __init__(self):
        self.__variants = 'AOY'
        self.__score = 0
        self.__sequence = choice(self.__variants)
    def wednesday(self):
        playsound.playsound('sounds/wednesday.mp3')

    def play(self):
        for letter in self.__sequence:
            playsound.playsound(f'sounds/{letter}.mp3')
    def check(self, guess):
        if guess == self.__sequence:
            playsound.playsound('sounds/correct.wav')
            self.__score += 1
            self.__next()
        elif guess != self.__sequence:
            playsound.playsound('sounds/incorrect.wav')
            self.__score -= 0.5


    def __next(self):
        if self.__score > 0:
            # self.__sequence += choice(self.__variants)
            __dlina = len(self.__sequence) + 1
            self.__sequence = ''
            for i in range(__dlina):
                self.__sequence += choice(self.__variants)

    def get_score(self):
        return self.__score
