
# * Графический интерфейс
# * import tkinter
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import winsound  # * генерация звука по кнопке
# # * <имя окна> = TK()
# root = Tk()
# # * <имя окна>.<имя свойства> = <значение окна>
# root.title('Мой пример')  # * Надпись в верхней части
# root.geometry('500x400+300+200')  # * размер и сдвиг
# # * Label - надпись
# # * Button - кнопка
# # * Entry - ввод
# # * Checkbutton - чекбокс с галочкой (с нескольким выбором)
# # * Radiobutton - чекбокс с одним выбором
# # * Listbox - выбор элемента
# # * Frame - рамка
# nadp = Label(root, text='Текст окна', font='Arial 18', bg='gray', fg='white')
# nadp.pack()
# button = Button(root, text='Моя кнопка!')
# button.pack()
# pale = Entry(root, width=20)
# pale.pack()
# tn_girn = Checkbutton(root, text='Полужирный', onvalue=1, offvalue=0)
# tn_girn.pack()
# per1 = Radiobutton(root, text='Мужчина', value=1)
# per1.pack()
# per2 = Radiobutton(root, text='Женщина', value=2)
# per2.pack()
# spisok = Listbox(root, height=4, width=20, selectmode=SINGLE)
# goroda = ['Подольск', 'Москва', 'СПБ', 'Анапа', 'Мадагаскар']
# for el in goroda:
#     spisok.insert(END, el)
# spisok.pack()
# ramka = Frame(root, width=500, height=50, bg='white')
# ramka.pack()
# ramka = Frame(root, width=500, height=50, bg='darkblue')
# ramka.pack()
# ramka = Frame(root, width=500, height=50, bg='darkred')
# ramka.pack()
# ramka.pack(side=TOP, expand=True)

# * генерация звука по кнопке


def Zvuk1():
    winsound.Beep(2000, 2000)


root = Tk()
root.title('Звук')
root.geometry('250x500+300+300')
knopka = Button(root, text='Нажми меня', command=Zvuk1)
knopka.pack()
# * .bind('<имя события>', имя функции для события)
# * <Button-1> - левая кнопка мыши
# * <Button-3> - правая кнопка мыши
# * <Retunr> - Enter
# * <Shift>
# * <Буква...>
# * <Control-a>


def Zvuk2(event):
    winsound.Beep(2000, 2000)


def Zvuk3(event):
    winsound.Beep(2500, 2000)


root.bind('<a>', Zvuk2)
knopka.bind('<Button-3>', Zvuk3)
root.mainloop()
