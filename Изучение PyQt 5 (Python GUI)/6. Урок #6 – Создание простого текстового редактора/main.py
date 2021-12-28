from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор кода")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        # занимает всю высоту и ширину окна
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        # open_file = fileMenu.addMenu("&Открыть")
        # save_file = fileMenu.addMenu("&Сохранить")
        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)

    # анатация, которая будет обрабатывать нажатия на различные пункты меню
    @QtCore.pyqtSlot()
    def action_clicked(self):
        # получение всей информации объекта
        action = self.sender()
        if action.text() == "Открыть":
            # [0] выбираем первый файл
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                with open(fname, "r", encoding="utf-8") as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                with open(fname, "w", encoding="utf-8") as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("No such file")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
