# Полный список см. man keysyms.

# Примеры
# <Button-1> или <1> - нажата левая клавиша мыши.

# <Alt-Motion> - движение мышью с нажатой на клавиатуре клавишей Alt.

# <Key> - нажатие любой клавиши на клавиатуре.

# Пример:

from tkinter import *
root=Tk()
def leftclick(event):
    print ('Вы нажали левую кнопку мыши')
def rightclick(event):
    print ('Вы нажали правую кнопку мыши')
button1=Button(root, text='Нажми')
button1.pack()
button1.bind('<Button-1>', leftclick)
button1.bind('<Button-3>', rightclick)
root.mainloop()