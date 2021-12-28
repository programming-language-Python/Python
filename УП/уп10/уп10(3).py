from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.geometry('200x90')


def yes():
    def e():
        ball = ['есть', 'нет', 'нет']
        rand = str(random.choices(ball))
        print(rand)
        if str(rand) == "['есть']":
            messagebox.showinfo(
                "Вы выиграли!!!", "В выбраном квадрате оказался шарик.")
        else:
            messagebox.showinfo(
                "Вы проиграли:(", "В выбраном квадрате не оказалось шарика.")
    root = Tk()
    root.geometry('500x300')
    lab1 = Label(
        root, text='На экране 3 квадрата.\nПод одним из них рандомно спрятан шарик.\nУгадай, где шарик.', font='arial 14')
    lab1.pack()
    Button(root, bg='black', command=e).place(
        width=100, height=100, relx=0.2, rely=0.3)
    Button(root, bg='black', command=e).place(
        width=100, height=100, relx=0.4, rely=0.3)
    Button(root, bg='black', command=e).place(
        width=100, height=100, relx=0.6, rely=0.3)
    root.mainloop()


lab = Label(root, text='Готов играть?', font='arial 14')
Button(root, text='да', width=2, height=1, bg='black', fg='green',
       font='arial 14', command=yes).place(relx=0.3, rely=0.3)
Button(root, text='нет', width=2, height=1, bg='black', fg='green',
       font='arial 14', command=root.destroy).place(relx=0.5, rely=0.3)

lab.pack()
root.mainloop()
