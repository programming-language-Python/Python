from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from калькулятор import Ui_Dialog
# Создание приложения
app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
# логика приложения


def bp(self):
    # при нажатии выводит текст 'Hello world'
    ui.lineEdit.setText('Hello world')


# вызывает функция при нажатии
ui.pushButton_10.clicked.connect(bp)
sys.exit(app.exec_())
