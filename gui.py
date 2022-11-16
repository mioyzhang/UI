import os
import sys
import time
import json
import typing
import random
import math

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QThread

from ui.edit import Ui_EditForm
from ui.terminal_mainwindow import Ui_TerminalMainWindow

from ui.ui_test import Ui_Form

from tools import generate_random_gps


class Test(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Test()
    w.show()

    app.exec()
