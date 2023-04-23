from tkinter import *

# def action():
#     print('Привет!')
#
#
#
root = Tk()


# Scale

# def get_scala(val):
#     # print(scala.get())
#     print(val)
#
#
# scala = Scale(root, from_=50, to=120, command=get_scala, orient=HORIZONTAL, length=300, tickinterval=10, resolution=10)
#
# scala.pack()

# root.geometry('400x300')
# root['bg'] = 'gray'
# lab = Label(root, text='21312')
# lab.pack()
# lab['bg'] = 'lightblue'
# lab['foreground'] = 'gold'
#
# ent = Entry(root, width=45, borderwidth=21)
#
# ent.pack()
# txt = Text(root, width=20, height=3, wrap='word')
# txt.pack()
#
# btn = Button(root, command=action)
# btn['text'] = 'Я кнопка'
# btn.pack()


# checkbutton
# def get_cb():
#     print(cb_val.get())
#
# cb_val = BooleanVar()
# cb = Checkbutton(root, text=';)',
#                  command=get_cb,
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False)
#
#
# cb.pack()


# radiobutton


# def get_rb():
#     print(rb_val.get())
#
#
# rb_val = IntVar()
# rb1 = Radiobutton(root, text='variant1.', variable=rb_val, value=421, command=get_rb)
# rb2 = Radiobutton(root, text='variant2.', variable=rb_val, value=124, command=get_rb)
# rb1.pack()
# rb2.pack()



# img = PhotoImage(file='cat.png')
# img_small = img.subsample(3, 3)
# img_big = img.zoom(3, 3)
# lab = Label(root, image=img)
# img_poltora = img.subsample(3, 3).zoom(2, 2)
# lab.pack()


# 1 задача


# def but(event):
#     val = ent.get()
#     lab['text'] = val
#     return lab
#
# root.geometry('400x500')
#
#
# lab = Label(root, text='000')
#
# lab.pack()
#
#
# ent = Entry(root)
# ent.bind('<Button-3>', but)
# ent.pack()


#2 задача

# def get_rb():
#     userchoose = rb_val.get()
#     if userchoose == 1:
#         lab['text'] = 'Hello World'
#
#     elif userchoose == 2:
#         lab['text'] = 'Hello Python'
#
#     return lab
#
root.geometry('300x400')
# lab = Label(root, text='Hello...')
# lab.pack()
#
# rb_val = IntVar()
# rb1 = Radiobutton(root, text='World', variable=rb_val, value=1, command=get_rb)
# rb2 = Radiobutton(root, text='Python', variable=rb_val, value=2, command=get_rb)
# rb1.pack()
# rb2.pack()



# Задача 3

# def get_cb():
#     user = cb_val.get()
#     if user == True:
#         btn['state'] = ['active']
#         btn['text'] = 'Активен!'
#     elif user == False:
#         btn['state'] = ['disabled']
#         btn['text'] = 'Не активен'
#
#
# cb_val = BooleanVar()
# cb = Checkbutton(root, text='Активировать',
#                  command=get_cb,
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False)
#
#
# cb.pack()
#
# btn = Button(root, command=get_cb, state=['disabled'])
# btn['text'] = 'Не активен'
# btn.pack()

# Задача 3.1


# def get_cb():
#     user = cb_val.get()
#     if user == True:
#         btn['state'] = ['active']
#         btn['text'] = 'Активен!'
#     elif user == False:
#         btn['state'] = ['disabled']
#         btn['text'] = 'Не активен'
#
#
# cb_val = BooleanVar()
# cb = Checkbutton(root, text='Активировать',
#                  command=get_cb,
#                  variable=cb_val,
#                  onvalue=False,
#                  offvalue=True)
#
#
# cb.pack()
#
# btn = Button(root, command=get_cb, state=['disabled'])
# btn['text'] = 'Не активен'
# btn.pack()








lab = Label(root, text='Я текст')
lab.pack()


def get_cb():
   user = cb_val.get()
   if user == 1:
       lab['font'] += 'bold'
   elif user == 2:
       pass

   if user == 7:
       lab['font'] += 'italic'

cb_val = IntVar()
bold = Checkbutton(root, text='Жирный',
                 command=get_cb,
                 variable=cb_val,
                 onvalue=1,
                 offvalue=2)
kurs = Checkbutton(root, text='Курсив',
                 command=get_cb,
                 variable=cb_val,
                 onvalue=3,
                 offvalue=4)
zach = Checkbutton(root, text='Зачеркнутый',
                 command=get_cb,
                 variable=cb_val,
                 onvalue=5,
                 offvalue=6)
podch = Checkbutton(root, text='Подчеркнутый',
                 command=get_cb,
                 variable=cb_val,
                 onvalue=7,
                 offvalue=8)


bold.pack()
kurs.pack()
zach.pack()
podch.pack()









root.mainloop()
