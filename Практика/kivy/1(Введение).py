from kivy.app import App
from kivy.uix.button import Button # подключение кнопки
from kivy.uix.codeinput import CodeInput # подсветка
# from pygments.lexers import HtmlLexer
# не меняет размер окна
from kivy.config import Config
Config.set('graphics','resizable','0')
# ширина и высота окна
Config.set('graphics','width','640')
Config.set('graphics','height','480')
# размер самой кнопки
from kivy.uix.floatlayout import FloatLayout
# работа с двумя пальцами
from kivy.uix.scatter import Scatter
class MyApp(App):
    def build(self): # метод
        s=Scatter()
        fl=FloatLayout(size=(300,300))
        # добавление FloatLayout в Scatter()
        s.add_widget(fl)
        # добавляем кнопку. Функции кнопки смотреть ниже
        fl.add_widget(Button(
            text='Это моя первая кнопка', 
            font_size=30,
            on_press=self.btn_press,
            background_color=[.33,.88,.14,1],
            background_normal='',
            # размер кнопки в % по отношению FloatLayout
            size_hint=(.5,.25),
            # позиция
            pos=(640/2-640/2/2,480/2-(480*.25/2))))
        # вместо fl возращаем s при использовании Scatter()
        return s
        # return CodeInput(Lexer=HtmlLexer())

        # создана кнопка на всё окно
        return Button(text='Это моя первая кнопка', 
        font_size=30,
        # выводит при нажатии функцию(событие при клике)
        on_press=self.btn_press,
        # background_color=[1,0,0,1], # кнопка тёмно-красная. Числа в процентах
        background_color=[.33,.88,.14,1],
        background_normal='') # теперь кнопка красная
    # сама функция, которая вызывется при нажатии
    def btn_press(self,instance): # instance - экземпляр
        print('Кнопка нажата!') # печатается в консоли
        instance.text='Я нажата' # меняет надпись кнопки
if __name__=="__main__":
    MyApp().run() # .run() запускает окно
# в uix находятся все виджеты

