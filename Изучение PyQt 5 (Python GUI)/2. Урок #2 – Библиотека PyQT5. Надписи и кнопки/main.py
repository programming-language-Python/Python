from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


# конструктор. Вызывается каждый раз при создании объекта
# на основе этого класса
class Window(QMainWindow):
    def __init__(self):
        # передача настроек в родительский класс
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        # первые два значения координаты(смещение), два других размеры
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        # позволяет размещать объект внутри окна
        self.main_text.move(100, 100)
        # подстаивает ширину объекта под содержимое
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_lable)

    def add_lable(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    # объект app нужен для создания приложения создаётся один раз
    # sys.argv все настройки пк на котором запускаем
    app = QApplication(sys.argv)
    window = Window()

    # появляется окно
    window.show()
    # программа будет всегда завершаться корректно
    sys.exit(app.exec_())


# если будем запускать файл как основной
if __name__ == "__main__":
    application()
