# bind_all - создаёт привязку для всех виджетов приложения. Отличие от привязки к окну верхнего уровня заключается в том,
# что в случае привязки к окну привязываются все виджеты этого окна, а этот метод привязывает все виджеты приложения
# (у приложения может быть несколько окон).
# bind_class - создаёт привязку для всех виджетов данного класса
# Пример:
'''
from tkinter import *
def callback(e):
    print ('Нажата кнопка', e.widget['text'])
root=Tk()
button1 = Button(root, text='1')
button1.pack()
button2 = Button(root, text='2')
button2.pack()
root.bind_class('Button', '<1>', callback)
root.mainloop()
'''
# bindtags - позволяет изменить порядок обработки привязок. По умолчанию порядок следующий: виджет, класс, окно, all;
# где виджет - привязка к виджету (bind),
# класс - привязка к классу (bind_class),
# окно - привязка к окну (root.bind),
# all - привязка всех виджетов (bind_all).
# Пример, меняем порядок обработки привязок на обратный:

from tkinter import *
def callback1(e): print ('callback1')
def callback2(e): print ('callback2')
def callback3(e): print ('callback3')
def callback4(e): print ('callback4')
root=Tk()
button = Button(root)
button.pack()
button.bind('<1>', callback1)
root.bind_class('Button', '<1>', callback2)
root.bind('<1>', callback3)
root.bind_all('<1>', callback4)
button.bindtags(('all', root, 'Button', button))
root.mainloop()

# unbind - отвязать виджет от события. В качестве аргумента принимает идентификатор, полученный от метода bind.
# unbind_all - то же, что и unbind, только для метода bind_all.
# unbind_class - то же, что и unbind, только для метода bind_class.