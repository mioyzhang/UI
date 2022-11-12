import os
import sys
import time
import json
import random
import math

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QThread

from ui.edit import Ui_EditForm
from ui.terminal_mainwindow import Ui_TerminalMainWindow

from tools import generate_random_gps


class TerminalMainWindow(QMainWindow, Ui_TerminalMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TerminalMainWindow()
    w.show()

    app.exec()
