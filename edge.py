import os
import sys
import time
import socket

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.Qt import QThread

from ui.edit import Ui_EditForm
from ui.terminal_mainwindow import Ui_TerminalMainWindow

from tools import generate_random_gps
from logic import *


class SocketThread(QThread):
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self, trigger):
        super(SocketThread, self).__init__()
        self.main_thread_trigger = trigger
        self.sock = socket.socket()
        self.dst = (socket.gethostname(), 8900)\

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

    def slot(self, arg: dict):
        print(f'QThread recv {arg}')
        if arg.get('type') == 'connect':
            self.connect()
        if arg.get('type') == 'test':
            self.test()
            # self.test_delay()
        if arg.get('type') == 'send':
            message = arg.get('context')
            self.send_message(message)

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


class TerminalMainWindow(QMainWindow, Ui_TerminalMainWindow):
    main_thread_trigger = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.listWidget_files.hide()
        self.listWidget_images.hide()

        self.init_connect()

    def init_connect(self):
        self.pushButton_position.clicked.connect(self.generate_random_gps)
        self.pushButton_generate.clicked.connect(self.generate_random_gps)
        self.pushButton_submit.clicked.connect(self.extract)

        self.toolButton_file.clicked.connect(self.choose_file)
        self.toolButton_img.clicked.connect(self.choose_image)

        self.listWidget_files.itemDoubleClicked['QListWidgetItem*'].connect(lambda: self.listWidget_files.takeItem(self.listWidget_files.currentRow()))
        self.listWidget_images.itemDoubleClicked['QListWidgetItem*'].connect(lambda: self.listWidget_images.takeItem(self.listWidget_images.currentRow()))

        self.pushButton_check.clicked.connect(self.connect)
        self.pushButton_send.clicked.connect(self.send)

        self.pushButton_set.clicked.connect(self.test)

        # 子线程信号与槽
        self.work_thread = SocketThread(self.main_thread_trigger)
        self.work_thread.trigger_in.connect(self.work_thread.slot)
        self.work_thread.trigger_out.connect(self.slot)
        self.work_thread.start()

    def test(self):
        self.work_thread.trigger_in.emit({'type': 'test'})

    def connect(self):
        self.work_thread.trigger_in.emit({'type': 'connect'})
        pass

    def generate_random_gps(self):
        longitude, latitude = generate_random_gps()
        self.lineEdit_gps.setText(f'{longitude}, {latitude}')

    def choose_file(self):
        file_filter = "All Files(*);;Text Files(*.txt)"
        filename = QFileDialog.getOpenFileNames(self, '选择文件', os.getcwd(), file_filter)
        filename = filename[0]
        self.listWidget_files.show()
        for i in filename:
            self.listWidget_files.addItem(i)
        print(filename)

    def choose_image(self):
        image_filter = "Image files (*.jpg *.png);;All Files(*)"
        imagename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), image_filter)
        imagename = imagename[0]
        self.listWidget_images.show()
        for i in imagename:
            self.listWidget_images.addItem(i)
        print(imagename)

    def extract(self):
        sequence = self.label_seq.text()
        type = self.comboBox.currentText()
        content = self.textEdit.toPlainText()
        with_gps = self.radioButton.isChecked()
        gps = self.lineEdit.text()

        files = [self.listWidget_files.item(i).text() for i in range(self.listWidget_files.count())]
        images = [self.listWidget_images.item(i).text() for i in range(self.listWidget_images.count())]

        self.message = Message(sequence, type, content, with_gps, gps, files, images)

    def slot(self, arg: dict):
        # if self.work_thread.started
        print(f'main recv: {arg}')

        pass

    def send(self):
        self.extract()
        signal = {
            'type': 'send',
            'context': self.message.to_json(),
            # 'context': self.message.to_json(),
        }
        print(self.message.to_json())
        self.work_thread.trigger_in.emit(signal)

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TerminalMainWindow()
    w.show()

    app.exec()
