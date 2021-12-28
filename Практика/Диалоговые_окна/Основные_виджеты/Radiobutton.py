# Виджет Radiobutton выполняет функцию, схожую с функцией виджета Checkbutton.
# Разница в том, что в виджете Radiobutton пользователь может выбрать лишь один из пунктов.
# Реализация этого виджета несколько иная, чем виджета Checkbutton:

from tkinter import *
root=Tk()
var=IntVar()
rbutton1=Radiobutton(root,text='1',variable=var,value=1)
rbutton2=Radiobutton(root,text='2',variable=var,value=2)
rbutton3=Radiobutton(root,text='3',variable=var,value=3)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
root.mainloop()
# В этом виджете используется уже одна переменная. В зависимости от того, какой пункт выбран, она меняет своё значение.
# Самое интересное, что если присвоить этой переменной какое-либо значение, поменяется и выбранный виджет.
# На этом мы прервём изучение типов виджетов (потом мы к ним обязательно вернёмся).