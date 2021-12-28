# Виджет Frame (рамка) предназначен для организации виджетов внутри окна. Рассмотрим пример:

from tkinter import *
root=Tk()
frame1=Frame(root,bg='green',bd=5)
frame2=Frame(root,bg='red',bd=5)
button1=Button(frame1,text='Первая кнопка')
button2=Button(frame2,text='Вторая кнопка')
frame1.pack()
frame2.pack()
button1.pack()
button2.pack()
root.mainloop()
# Свойство bd отвечает за толщину края рамки.