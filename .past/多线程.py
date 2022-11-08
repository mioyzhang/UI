import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QThread

from ui.form_ui import Ui_Form


class MyThread(QThread):
    thread_signal = pyqtSignal(str)

    def __init__(self, signal):
        super(MyThread, self).__init__()
        self.login_signal = signal

    def login_by_request(self, user_info):
        print(f'QThread: {user_info}')
        time.sleep(3)
        self.login_signal.emit('login success')

    def run(self) -> None:
        while True:
            print('QThread...')
            time.sleep(1)


class MyWindow(QWidget, Ui_Form):
    main_signal = pyqtSignal(str)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('icon/cat.png'))
        self.login_thread = MyThread(self.main_signal)
        self.login_thread.start()

        self.init_signal()

    def init_signal(self):

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.login2)

        self.main_signal.connect(self.login_status)

        self.login_thread.thread_signal.connect(self.login_thread.login_by_request)

    def login(self):
        username = self.LineEdit.text()
        password = self.LineEdit_2.text()
        print(f'username: {username}\npassword: {password}')
        self.textBrowser.setText(f'username: {username}\npassword: {password}')

    def login2(self):
        username = self.LineEdit.text()
        password = self.LineEdit_2.text()
        self.login_thread.thread_signal.emit(f'username: {username}\npassword: {password}')

    def login_status(self, status):
        print(f'status: {status}')
        self.textBrowser.setText(f'status: {status}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
