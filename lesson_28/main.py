from tkinter import *

# root = Tk()
#
# lab = Label(root, text='голубой')
# ent = Entry(root, text='#007dff')
# empty = Label(root)
# lab.pack()
#
# ent.pack()
# empty.pack()
#
#
#
#
# red = Button(root,
#              bg='red',
#             width=20,
#              height=2,
#              )
# orange = Button(root,
#              bg='orange',
#             width=20,
#              height=2,
#              )
# yellow = Button(root,
#              bg='yellow',
#             width=20,
#              height=2,
#              )
# green = Button(root,
#              bg='#00ff23',
#             width=20,
#              height=2,
#              )
# lightblue = Button(root,
#              bg='#00fff0',
#             width=20,
#              height=2,
#              )
# blue = Button(root,
#                  bg='blue',
#                  width=20,
#                  height=2,
#
#              )
# purple = Button(root,
#              bg='purple',
#             width=20,
#              height=2,
#              )
# red.pack()
# empty.pack()
# orange.pack()
# empty.pack()
# yellow.pack()
# empty.pack()
# green.pack()
# empty.pack()
# lightblue.pack()
# empty.pack()
# blue.pack()
# empty.pack()
# purple.pack()
#
#
#
#
#
#
#
#
#
#
#
# root.mainloop()


# def console():
#     message = ent.get()
#     msg = txt.get(1.0, END)
#     ent.delete(0,END)
#     txt.delete(1.0,END)
#     print('Комментарий:', msg)
#     print('Откуда: ', message)
#
#
#
#
#
# root = Tk()
#
# lab = Label(root, text='Ваш адрес:',
#             bg= 'white') # надпись
# lab.pack()
# ent = Entry(root, width=20, bd=5)
# ent.pack()
# root.geometry('500x400')
#
# lab2 = Label(root, text='Комментарий:')
# lab2.pack()
# txt = Text(root,
#               width=18,  # ширина в символах
#               height=5,  #  высота в символах
#               font="Verdana 14",  # шрифт
#               wrap="word"   # перенос
#               )
# txt.pack()
#
# btn = Button(root,
#              text='Отправить',
#              bg='lightblue',
#              width=20,
#              height=2,
#              command=console,
#              )
#
# btn.pack()
#
# root.mainloop()






root = Tk()


base = Label(root, text='Привет')

info = base["font"] = "Arial, 15,  bold"



root.geometry('500x400')


base.pack()



root.mainloop()















































# def h_ell_o(event):
#    message = ent.get()
#    msg = txt.get('start',"end-1c")
#    ent.delete(0,END)
#    txt.delete(0,END)
#    print(message)
#    print(msg)
#
#
# root = Tk() # создание/инициализация
# #
# root.title('---')
#
# lab = Label(root, text='Ваш адрес:',
#             bg= 'white') # надпись
#
# root.geometry('500x400')
#
# lab.pack() #размечаем элемент
#
#
# # lab['background'] = 'black'
# # lab['foreground'] = 'white'
#
# #
# # lab['bg'] = 'white smoke'
# # lab['fg'] = 'black'
# # lab['font'] = 20 #размер шрифта
# # lab['font'] = ('Calibri', 20, 'italic', 'underline', 'overstrike')
# # lab['height'] =5
# # lab['width'] = 20
# ent = Entry(root, width=30, bd=5)
# ent.pack()
#
#
# lab2 = Label(root, text='Комментарий:')
# lab2.pack()
# txt = Text(root,
#               width=18,  # ширина в символах
#               height=5,  #  высота в символах
#               font="Verdana 14",  # шрифт
#                   wrap="word"   # перенос
#               )
# txt.pack()
#
# btn = Button(root,
#              text='Отправить',
#              bg='lightblue',
#             width=20,
#              height=2,
#              # command=h_ell_o,
#              )
#
#
#
#
# btn.pack()
# btn.bind('<Button-1>',h_ell_o)
# #Button1 - ЛКМ
# #Button3 - ПКМ
#
#
#
# #
# red = Button(root,
#              bg='red',
#             width=20,
#              height=2,
#              )
# orange = Button(root,
#              bg='orange',
#             width=20,
#              height=2,
#              )
# yellow = Button(root,
#              bg='yellow',
#             width=20,
#              height=2,
#              )
# green = Button(root,
#              bg='#00ff23',
#             width=20,
#              height=2,
#              )
# lightblue = Button(root,
#              bg='#00fff0',
#             width=20,
#              height=2,
#              )
# blue = Button(root,
#                  bg='blue',
#                  width=20,
#                  height=2,
#
#              )
# purple = Button(root,
#              bg='purple',
#             width=20,
#              height=2,
#
#              )
# red.pack()
# orange.pack()
# yellow.pack()
# green.pack()
# lightblue.pack()
# blue.pack()
# purple.pack()
#
#
#
# root.mainloop() #после ничего не писать
