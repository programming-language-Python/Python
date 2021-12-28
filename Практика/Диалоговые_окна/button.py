from tkinter import *
def button_clicked():
    print ("Клик!")
root=Tk()
# кнопка по умолчанию
button1 = Button()
button1.pack()
# именованные аргументы, конфигурирующие виджет. Это может быть используемый шрифт (font=...), цвет виджета (bg=...),
# команда, выполняющаяся при активации виджета (command=...) и т.д. Полный список всех аргументов можно посмотреть
# в man options и man-странице соответствующего виджета (например man button, см. разделы "STANDARD OPTIONS" и "WIDGET-SPECIFIC OPTIONS")

# кнопка с указанием родительского виджета и несколькими аргументами
button2 = Button(root, bg="red", text="Кликни меня!", command=button_clicked)
button2.pack()
root.mainloop()