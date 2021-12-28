# Checkbutton - это виджет, который позволяет отметить „галочкой“ определенный пункт в окне.
# При использовании нескольких пунктов нужно каждому присвоить свою переменную.
# Разберем пример:

from tkinter import *
root=Tk()
var1=IntVar()
var2=IntVar()
check1=Checkbutton(root,text='1 пункт',variable=var1,onvalue=1,offvalue=0)
check2=Checkbutton(root,text='2 пункт',variable=var2,onvalue=1,offvalue=0)
check1.pack()
check2.pack()
root.mainloop()
# IntVar() - специальный класс библиотеки для работы с целыми числами. variable - свойство,
# отвечающее за прикрепление к виджету переменной. onvalue, offvalue - свойства,
# которые присваивают прикреплённой к виджету переменной значение,
# которое зависит от состояния(onvalue - при выбранном пункте, offvalue - при невыбранном пункте).