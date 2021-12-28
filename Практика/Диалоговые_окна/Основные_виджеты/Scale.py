# Scale (шкала) - это виджет, позволяющий выбрать какое-либо значение из заданного диапазона. Свойства:

# orient - как расположена шкала на окне. Возможные значения: HORIZONTAL, VERTICAL (горизонтально, вертикально).
# length - длина шкалы.
# from_ - с какого значения начинается шкала.
# to - каким значением заканчивается шкала.
# tickinterval - интервал, через который отображаются метки шкалы.
# resolution - шаг передвижения (минимальная длина, на которую можно передвинуть движок)
# Пример кода:

from tkinter import *
root = Tk()
def getV(root):
    a = scale1.get()
    print ("Значение", a)
scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=50,to=80,tickinterval=5,resolution=5)
button1 = Button(root,text="Получить значение")
scale1.pack()
button1.pack()
button1.bind("<Button-1>",getV)
root.mainloop()
# Здесь используется специальный метод get(), который позволяет снять с виджета определенное значение, и используется не только в Scale.