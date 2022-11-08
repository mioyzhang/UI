import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('ui/form_ui.ui')
        print(self.ui.__dict__)
        for i, j in self.ui.__dict__.items():
            print(i, j)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()

    app.exec()
