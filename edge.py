import os
import sys
import time
import json
import socket

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.Qt import QThread

from ui.editForm import Ui_EditForm
from ui.edgeWindow import Ui_EdgeMainWindow

from tools import *
from logic import Logic, Message


class SocketThread(QThread):
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self, trigger):
        super(SocketThread, self).__init__()
        self.main_thread_trigger = trigger
        self.sock = socket.socket()
        self.dst = (socket.gethostname(), 8900)

        self.connection = False

    def test(self):
        print('test')
        self.trigger_out.emit({'back': 'test'})

    def connect(self):
        try:
            self.sock.connect(self.dst)
            back = {
                'type': 'connect',
                'status': True
            }
            self.trigger_out.emit(back)
            self.connection = True
            return True
        except ConnectionError as e:
            back = {
                'type': 'connect',
                'status': False,
                'context': str(e)
            }
            print(e)
            self.trigger_out.emit(back)
            return False

    def slot(self, args: dict):
        print(f'Thread <-- {args}')
        type_ = args.get('type')
        context = args.get('context')

        if args.get('type') == 'connect':
            self.connect()

        if type_ == SIGNAL_CHECK:
            dest = args.get('dest')
            port = args.get('port')

        if type_ == SIGNAL_SEND:
            dest = args.get('dest')
            protocol = args.get('protocol')

    def test_delay(self):
        current_time = time.time()
        message_dict = {
            'type': 'test',
            'time': current_time
        }
        message = json.dumps(message_dict)
        self.send_message(message)

    def send_message(self, message):
        print(f'try send {message}')
        try:
            self.sock.send(message.encode())
            back = {
                'type': 'send',
                'status': True
            }
            print(back)
            self.trigger_out.emit(back)
            return True
        except ConnectionError as e:
            back = {
                'type': 'send',
                'status': False,
                'context': str(e)
            }
            print(back)
            self.trigger_out.emit(back)
            return False

    def run(self):
        while True:
            time.sleep(1)


class TerminalMainWindow(QMainWindow, Ui_EdgeMainWindow):
    main_thread_trigger = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.work_thread = None
        self.sequence = 0

        self.setupUi(self)
        self.init_connect()

        # temporary use
        self.editwidget.label_seq.setText(f'{self.sequence:0>8d}')

    def init_connect(self):

        self.pushButton_check.clicked.connect(self.check_connect)
        # self.pushButton_test2.clicked.connect(self.test)

        # self.editwidget.pushButton_submit.clicked.connect(self.send)
        self.pushButton_send.clicked.connect(self.send)

        # 子线程信号与槽
        self.work_thread = SocketThread(self.main_thread_trigger)
        self.work_thread.trigger_in.connect(self.work_thread.slot)
        self.work_thread.trigger_out.connect(self.slot)
        self.work_thread.start()

    def test(self):
        print('test')
        # self.work_thread.trigger_in.emit({'type': 'test'})

    def check_connect(self):
        signal = {
            'type': SIGNAL_CHECK,
            'dest': self.lineEdit_c_address.text(),
            'port': self.lineEdit_c_port.text(),
        }
        print(f'main   --> {signal}')
        self.work_thread.trigger_in.emit(signal)

    def slot(self, arg: dict):
        # if self.work_thread.started
        print(f'main recv: {arg}')

        pass

    def send(self):
        self.editwidget.extract()
        message = self.editwidget.message

        address = '127.0.0.1'
        if self.radioButton_address.isChecked():
            address = self.lineEdit_address.text()
        protocol = self.comboBox_protocol.currentText()

        signal = {
            'type': SIGNAL_SEND,
            'context': message.to_json(),
            'dest': address,
            'protocol': protocol
        }
        print(f'main   --> {message.to_json()}')
        self.work_thread.trigger_in.emit(signal)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TerminalMainWindow()
    w.show()

    app.exec()
