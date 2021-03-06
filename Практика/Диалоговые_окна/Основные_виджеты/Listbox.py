# Listbox - это виджет, который представляет собой список, из элементов которого пользователь
# может выбирать один или несколько пунктов. Имеет дополнительное свойство selectmode, которое,
# при значении SINGLE, позволяет пользователю выбрать только один элемент списка, а при значении EXTENDED - любое количество. Пример:

from tkinter import *
root=Tk()
listbox1=Listbox(root,height=5,width=15,selectmode=EXTENDED)
listbox2=Listbox(root,height=5,width=15,selectmode=SINGLE)
list1=["Москва","Санкт-Петербург","Саратов","Омск"]
list2=["Канберра","Сидней","Мельбурн","Аделаида"]
for i in list1:
    listbox1.insert(END,i)
for i in list2:
    listbox2.insert(END,i)
listbox1.pack()
listbox2.pack()
root.mainloop()
# Стоит заметить, что в этой библиотеке для того, чтобы использовать русские буквы в строках,
# нужно использовать Unicode-строки. В Python 2.x для этого нужно перед строкой поставить букву u,
# в Python 3.x этого делать вообще не требуется, т.к. все строки в нем изначально Unicode.
# Кроме того в первой или второй строке файла необходимо указать кодировку файла (в комментарии): coding: utf-8.
# Чаще всего используется формат в стиле текстового редактора emacs:

# encoding: utf-8
# В Python 3.x кодировку файла можно не указывать, в этом случае по умолчанию предполагается utf-8.