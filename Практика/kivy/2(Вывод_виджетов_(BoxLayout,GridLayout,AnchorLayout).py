# Всего Layout 8
# GridLayout подойдёт для калькулятора

# BoxLayout - вывод коробками
# GridLayout - работает как таблица
# AnchorLayout - располагает виджет по 9 точкам (LB,CB,RB,LC,CC,RC,LT,CT,RT)

# запуск kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# пустой виджет. Можно создать свой
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

# в конце названия класса обязательно должен быть App
class BoxApp(App):
    def build(self):
        # BoxLayout
        # bl занимает всё прстранство окна
        # orientation меняет ориентацию по умолчанию по горизонтали(horizontal)
        # второй аргумент отступ (css) (padding=[50,25] - в kivy это внешний отступ)
        # spacing увеличивает растояние между виджетами
        # bl=BoxLayout(orientation='horizontal', spacing=100)

        # передаём виджет
        # bl.add_widget( Button(text='Кнопка 1') )
        # bl.add_widget( Button(text='Кнопка 2') )
        # bl.add_widget( Button(text='Кнопка 3') )

        # GridLayout
        # cols - количество колонок, rows - количество строк
        # bl=GridLayout(rows=5,cols=5,padding=[30],spacing=3)
        # если в цикле написать число больше произведения rows*cols то выдаст ошибку
        # for x in range(30):
            # bl.add_widget( Button(text='x') )

        # AnchorLayout. Может применяться в авторизации
        # если точки не указывать то по умолчанию располагается по центру
        # bl=AnchorLayout(anchor_x='left', anchor_y='top')
        # bl.add_widget( Button(text='Button',size_hint=[.5,.5]) )

        # авторизация
        # al=AnchorLayout()
        # можно вместо size_hint(имеет больший приоритет) написать size (ед. изм. px)
        # или написать size_hint=[None,None], size=[300,200]
        # bl=BoxLayout(orientation='vertical', size_hint=[.4,.4])
        # bl=BoxLayout(orientation='vertical', size_hint=[None,None], size=[300,200])

        # bl.add_widget( TextInput() )
        # bl.add_widget( TextInput() )
        # bl.add_widget( Button(text='Войти') )
        # al.add_widget(bl)
        # return al

        # калькулятор
        gl=GridLayout(cols=4, padding=[35], spacing=3)
        
        gl.add_widget( Button(text='7') )
        gl.add_widget( Button(text='8') )
        gl.add_widget( Button(text='9') )
        gl.add_widget( Button(text='x') )

        gl.add_widget( Button(text='4') )
        gl.add_widget( Button(text='5') )
        gl.add_widget( Button(text='6') )
        gl.add_widget( Button(text='-') )

        gl.add_widget( Button(text='1') )
        gl.add_widget( Button(text='2') )
        gl.add_widget( Button(text='3') )
        gl.add_widget( Button(text='+') )

        gl.add_widget( Widget() )
        gl.add_widget( Button(text='0') )
        gl.add_widget( Button(text='.') )
        gl.add_widget( Button(text='=') )
        return gl

        # return bl
# проверка если запускаем из консоли то в name будет содержаться main
# если подключаем из другого python кода тогда name будет содержать имя модуля
if __name__=="__main__":
    # run() появился потому что BoxApp у наследовал у App 
    BoxApp().run()