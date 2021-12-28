# root.destroy - Уничтожение виджета и всех его потомков. Стоит отметить, что если необходимо только
# на время спрятать какой-либо виджет, то лучше пользоваться упаковщиком grid и методом grid_remove:
from tkinter import *
def hide_show():
    if label.winfo_viewable():
# Использование grid_remove позволяет сохранять взаимное расположение виджетов.
# при нажатии на кнопку текст пропадает
       label.grid_remove()
    else:
        label.grid()
root=Tk()
label = Label(text='Я здесь!')
label.grid()
button = Button(command=hide_show, text="Спрятать/показать")
button.grid()
root.mainloop()