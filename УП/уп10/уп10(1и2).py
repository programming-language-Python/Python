from tkinter import *
import turtle
t = turtle.Pen()
t.shape("turtle")
p = 'right'
t.down()
# p - переменная обозначает куда была направлена черепашка (предыдущее направление)
# нажата - обозначает какая клавиша была нажата


def off(event):
    t.up()


def on(event):
    t.down()


def help(нажата):
    global p
    c = 90
    m = -1

    if p == 'up' or p == 'down':
        if нажата == 'l':
            t.left(c)
        elif нажата == 'r':
            t.left(m*c)

    if p == 'left':
        if нажата == 'u' or нажата == 'd':
            t.left(m*c)
        elif нажата == 'r':
            t.left(2*m*c)

    if p == 'right':
        if нажата == 'u' or нажата == 'd':
            t.left(c)
        elif нажата == 'l':
            t.left(2*c)
    '''
    # p=up or p=down
    if (p=='up' or p=='down') and нажата=='l':
        t.left(c)
    elif (p=='up' or p=='down') and нажата=='r':
        t.left(m*c)
    
    # p=left
    if p=='left' and (нажата=='u' or нажата=='d'):
        t.left(m*c)
    elif p=='left' and нажата=='r':
        t.left(2*m*c)
    
    # p=right
    if p=='right' and (нажата=='u' or нажата=='d'):
        t.left(c)
    elif p=='right' and нажата=='l':
        t.left(2*c)
    '''
    if нажата == 'd':
        t.backward(50)
    else:
        t.forward(50)


root = Tk()
# параметр передаётся объект события(event), в нём содержится информация о событии,
# например координаты мыши относительно окна (event.x,event.y) или координаты мыши относительно экрана (event.x_root,event.y_root)


def up(event):
    global p
    help('u')
    p = 'up'
    print('up')


def down(event):
    global p
    help('d')
    p = 'down'
    print('down')


def left(event):
    global p
    help('l')
    p = 'left'
    print('left')


def right(event):
    global p
    help('r')
    p = 'right'
    print('right')


button1 = Button(root, text='on', width=25, height=5,
                 bg='black', fg='red', font='arial 14')
button2 = Button(root, text='off', width=25, height=5,
                 bg='black', fg='red', font='arial 14')

button1.bind("<Button-1>", on)
button2.bind("<Button-1>", off)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Left>', left)
root.bind('<Right>', right)
button1.pack()
button2.pack()
root.mainloop()
