from tkinter import *

root = Tk()

c = Canvas(root, width=450, height=450, bg='white')
c.pack(anchor=CENTER, expand=True)

# '-------------- ЗАДАЧИ -------------------'

# root.geometry('1000x1000')

#
# pyimg = PhotoImage(file='tt.png')
# sec = 0
# def counter():
#     global sec
#     c.delete('all')
#     sec = sec + 1
#     if sec == 15:
#         root.destroy()
#     c.create_text(int(c['width']) / 2, int(c['height']) / 2, text=sec, font=('Arial 50', 120))
#     c.create_image(int(c['width']) / 2, int(c['height']) / 2, image=pyimg)
#     root.after(1000, counter)
#
#
#
# c.create_image(int(c['width']) / 2, int(c['height'])/2, image=pyimg)
# c.create_text(int(c['width']) / 2, int(c['height'])/2, text=sec, font=('Arial 50', 120))
#
# root.after(1000, counter)


# root.geometry('800x200')
#
#
#
#
# c.create_text(50, 20, text='Школа', font=('Arial 50', 25))
#
#
# c.create_line(115, 20, 200, 20, width=5, arrow='last')
#
# c.create_text(300, 20, text='туда-сюда', font=('Arial 50', 25))
#
# c.create_line(400, 20, 485, 20, width=5, arrow='last')
#
# c.create_text(600, 20, text='Успех 100%', font=('Arial 50', 25))


root.geometry('500x500')


l = None
p = None


def lh(event):
    global l
    l = event.x, event.y
    return l

def rh(event):
    global p
    p = event.x, event.y
    return p

def build():
    c.create_line(p[0], p[1], l[0], l[1])




btn = Button(root, text='лляля', command=build)
btn.pack()
c.bind('<Button-1>', lh)
c.bind('<Button-3>', rh)






















## -- TEXT --
# c.create_text(200, 200, text="😘 😥 😅 😎",font="Arial 24", fill='magenta', anchor=NW)

## -- RECTNGLE --

# c.create_rectangle(10,10,150,100,fill='gray', outline='white', width = 7)

## -- POLYGON --

# c.create_polygon(10, 10,
#                  10, 90,
#                  140, 90)  # 3 точки

## -- OVAL --

# c.create_oval(10, 10,
#               150, 250,
#               fill='red',
#               outline='white')

# -- ARC --

# c.create_arc(10, 10, 150, 150, extent=180, fill='red', outline='black')


# -- PACMAN --

# c.create_arc(10, 10, 150, 150, extent=300, fill='gold', outline='black')
#
# c.create_text(100, 50, text='O', fill='black')
# c.create_text(100, 50, text='o', fill='black')
# c.create_text(100, 50, text='·', fill='black')
# c.create_text(101, 49, text='o', fill='black')
# c.create_text(100, 49, text='o', fill='black')
# c.create_text(101, 50, text='o', fill='black')
# c.create_text(101, 49, text='·', fill='black')
# c.create_text(100, 49, text='·', fill='black')
# c.create_text(101, 50, text='·', fill='black')
#
#
# c.create_text(150, 120, text='O', fill='gold')
# c.create_text(150, 120, text='o', fill='gold')
# c.create_text(150, 120, text='·', fill='gold')
# c.create_text(151, 119, text='o', fill='gold')
# c.create_text(151, 119, text='·', fill='gold')
# c.create_text(151, 119, text='o', fill='gold')
# c.create_text(151, 119, text='·', fill='gold')
# c.create_text(151, 120, text='o', fill='gold')
# c.create_text(151, 120, text='·', fill='gold')
#
#
#
#
#
# c.create_text(250, 220, text='O', fill='gold')
# c.create_text(250, 220, text='o', fill='gold')
# c.create_text(250, 220, text='·', fill='gold')
# c.create_text(251, 219, text='o', fill='gold')
# c.create_text(251, 219, text='·', fill='gold')
# c.create_text(250, 219, text='o', fill='gold')
# c.create_text(250, 219, text='·', fill='gold')
# c.create_text(251, 220, text='o', fill='gold')
# c.create_text(251, 220, text='·', fill='gold')
#
#
#
#
# c.create_text(350, 320, text='O', fill='gold')
# c.create_text(350, 320, text='o', fill='gold')
# c.create_text(350, 320, text='·', fill='gold')
# c.create_text(351, 319, text='o', fill='gold')
# c.create_text(351, 319, text='·', fill='gold')
# c.create_text(350, 319, text='o', fill='gold')
# c.create_text(350, 319, text='·', fill='gold')
# c.create_text(351, 320, text='o', fill='gold')
# c.create_text(351, 320, text='·', fill='gold')


# -- хорда --

# c.create_arc(10,10,
#              150,150,
#              extent=300,
#              start=45,
#              style=CHORD)


# -- дуга --


# c.create_arc(10,10,
#              150,150,
#              extent=300,
#              start=45,
#              style=ARC,
#              outline= 'red')


# c.create_arc(10,10,
#              150,150,
#              extent=300,
#              start=45,
#              fill='lightgray',
#              outline='black',
#              dash='-.-',
#              activefill='white')


# event

# def ch(event):
#     print(event.x, event.y)
#
#
# btn = Button(root, text='button')
# btn.pack()
# btn.bind('<Button-3>', ch)


root.mainloop()
