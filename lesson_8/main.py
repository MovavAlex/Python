# import random # подтянуть в проект библиотеку
# print(random.randint(0,100)) # 0 <-- x <= 100
#
#import random as r  # r = random
#print(r.randint(0,100))

# from random import randint #подтянуть ТОЛЬКО randint из random
# print(randint(0,100))

#from random import * # импортировать всё из модуля ( Это Плохо )
#print(randint(0, 100))

#import random as r
#lst = [0,1,2,3,4,5]
#print(r,choice(lst))
#r.shuffle(lst)
#print(lst)

import turtle
screen = turtle.Screen() #экран
t = turtle.Turtle() #черепашка
t.pensize(3)
horizontal = 200
vertical = 100
t.speed(4)
t.shape("turtle")


t.color("blue","red")
#t.forward(100)

# t.back(100)
# t.right(100)
# t.forward(100)
# t.left(100)
# t.forward(300)
# t.left(100)
# t.forward(100)
# t.left(80)
# t.forward(250)

t.begin_fill() #начало закрашивания
t.fd(horizontal)
t.right(90)
t.fd(vertical)
t.rt(90)
t.fd(horizontal)
t.rt(90)
t.fd(vertical)
t.rt(90)
t.end_fill()

t.speed(5)
t.penup()#поднять перо
t.goto(0,-50)
t.pendown()#опустить перо
t.fd(205)

t.circle(100)

t.write("Круг с текстам", font = ("Arial BLack", 25, "normal"))

screen.exitonclick() #выйти по клику