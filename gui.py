import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QThread

from ui.MainWindow_ui import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('resource/icon/cat.png'))
        self.init_connect()

    def init_connect(self):
        self.listWidget.currentRowChanged.connect(lambda x: self.stackedWidget.setCurrentIndex(x))

    def test(self, current_row):
        self.stackedWidget.setCurrentIndex(current_row)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
