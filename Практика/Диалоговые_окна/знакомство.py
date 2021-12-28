from tkinter import *
# messagebox – стандартные диалоговые окна
from tkinter.messagebox import *
root=Tk()
# showinfo() 1 аргумент заголовок окна 2 аргумент текст окна
# fond - высота шрифта
btn1=Button(root,text='Info',font=('Ubuntu',20),command=lambda: showinfo('Заголовок','Информация'))
#  атрибут sticky (липкий), который принимает значения направлений сторон света (N, S, W, E, NW, NE, SW, SE)
btn1.grid(row=0,column=0,sticky='ew') # вывод окна

btn2=Button(root,text='Warning',font=('Ubuntu',20),command=lambda: showwarning('ShowWarning','Предупреждение'))
btn2.grid(row=1,column=0,sticky='ew')

btn3=Button(root,text='Error',font=('Ubuntu',20),command=lambda: showerror('ShowError','Предупреждение'))
btn3.grid(row=2,column=0,sticky='ew')

root.mainloop()