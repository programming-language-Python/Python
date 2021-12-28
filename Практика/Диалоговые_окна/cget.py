# Метод cget является обратным к методу configure. Он предназначен для получения информации о конфигурации виджета.
# Здесь как и в случае с configure можно использовать квадратные скобки (value = widget['option']).
# Пример, после клика на кнопку программа показывает цвет кнопки и меняет его на другой:
from tkinter import *
from random import random
def button_clicked():
    button['text'] = button['bg'] # показываем предыдущий цвет кнопки
    bg = '#%0x%0x%0x' % (int(random()*16), int(random()*16), int(random()*16))
    button['bg'] = bg
    button['activebackground'] = bg # цвет при нажатии
root=Tk()
button = Button(root, command=button_clicked)
button.pack()
root.mainloop()