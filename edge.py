import os
import sys
import time
import json
import socket
import threading

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.Qt import QThread

from ui.editForm import Ui_EditForm
from ui.edgeWindow import Ui_EdgeMainWindow

from tools import *
from logic import Logic, Message, Packet
from transfer import TransferThread


class SocketThread(TransferThread):
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self):
        super(SocketThread, self).__init__()

    def test(self):
        print('test')
        self.trigger_out.emit({'back': 'test'})

    def connect(self, address=None):
        if not address:
            address = ('127.0.0.1', LISTENING_PORT)

        if self.connected:
            if self.connected[0] == address[0]:
                if self.connected[1] != address[1]:
                    back = {
                        'type': BACK_REPLAY,
                        'status': PORT_MODIFY,
                        'address': self.connected[0],
                        'port': self.connected[1]
                    }
                    self.trigger_out.emit(back)

                return True

            else:
                print(f'disconnect {self.connected}')
                self.client.close()
                self.connected = None
                self.client = socket.socket()
        
        print(f'try to connect to {address}')
        try:

            self.client.connect(address)
            self.connected = address
            return True
        
        except BaseException as e:
            back = {
                'type': BACK_REPLAY,
                'status': CONNECT_FAIL,
                'error': str(e)
            }
            print(e)
            self.trigger_out.emit(back)
            self.client = socket.socket()
            return False

    def test_delay(self, address):
        if not self.connect(address):
            return False

        message_dict = {
            'type': 'test',
            'time': time.time()
        }
        message = json.dumps(message_dict)
        if self.send(message):
            recv = self.client.recv(2048).decode()
            recv = json.loads(recv)

            past_time = recv.get('time')
            delay = time.time() - past_time

            back = {
                'type': BACK_DELAY,
                'delay': delay
            }
            print(f'Thread  --> {back}')
            self.trigger_out.emit(back)
            return False
            
        else:
            pass
    
    def send_message(self, message, ):
        pass

    def slot(self, args: dict):
        print(f'Thread <-- {args}')
        type_ = args.get('type')
        context = args.get('context')

        if type_ == SIGNAL_SEND:
            dest = args.get('dest')
            protocol = args.get('protocol')
            context = args.get('context')

            msg = Message(context)
            pkg = Packet(dst=dest, message=msg)
            self.send()

        if type_ == SIGNAL_CHECK:
            dest = args.get('dest')
            port = args.get('port')
            self.test_delay((dest, port))

    def send(self, message, success_signer=False):
        print(f'send {message} to {self.connected}')
        try:
            self.client.send(message.encode())
            print(f'send {message} to {self.connected} success')
            if success_signer:
                back = {
                    'type': BACK_SEND,
                    'status': SEND_SUCCESS,
                    'context': message
                }
                self.trigger_out.emit(back)
            return True
        except BaseException as e:
            back = {
                'type': BACK_REPLAY,
                'status': SEND_ERROR,
                'context': message,
                'error': str(e)
            }
            print(f'Thread  --> {back}')
            self.trigger_out.emit(back)
            return False

    def run(self):
        while True:
            time.sleep(1)
        
        self.server.bind(('0.0.0.0', 8900))
        self.server.listen(5)

        while True:
            client, address = self.server.accept()
            print(f'{address} connected')
            # signal = {
            #     'type': 'connect',
            #     'address': address
            # }
            # self.child_thread_trigger.emit(signal)

            p = threading.Thread(target=self.recv, args=(client, address))
            # p = RecvThread(client, address)
            p.start()

class EdgelMainWindow(QMainWindow, Ui_EdgeMainWindow):
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
        # self.pushButton_test.clicked.connect(self.check_delay)

        # self.editwidget.pushButton_submit.clicked.connect(self.send)
        self.pushButton_send.clicked.connect(self.send)

        self.pushButton_turn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # 子线程信号与槽
        self.work_thread = SocketThread()
        self.work_thread.trigger_in.connect(self.work_thread.slot)
        self.work_thread.trigger_out.connect(self.slot)
        self.work_thread.start()

    def test(self):
        print('test')
        # self.work_thread.trigger_in.emit({'type': 'test'})

    def check_connect(self):
        self.pushButton_set.setChecked(False)
        self.lineEdit_c_address.setEnabled(False)
        self.lineEdit_c_port.setEnabled(False)

        signal = {
            'type': SIGNAL_CHECK,
            'dest': self.lineEdit_c_address.text(),
            'port': int(self.lineEdit_c_port.text()),
        }
        print(f'main   --> {signal}')
        self.work_thread.trigger_in.emit(signal)
    
    def view_delay(self, delay):
        delay = delay * 10 ** 3 / 2
        self.label_delay.setText(f'{delay:.3f} ms')

        self.label_status.setText('connected')
        self.label_status.setStyleSheet("color:green;"); 

    def slot(self, args: dict):
        # if self.work_thread.started
        print(f'main   <-- {args}')
        type_ = args.get('type')

        if type_ == BACK_SEND:
            status = args.get('status')
            context = args.get('context')

        if type_ == BACK_DELAY:
            delay = args.get('delay')
            self.view_delay(delay)
        
        if type_ == BACK_REPLAY:
            status = args.get('status')

            if status == PORT_MODIFY:
                port = args.get('port')
                self.lineEdit_c_port.setText(f'{port}')
                # self.pushButton_set.
            
            if status == CONNECT_FAIL:
                error = args.get('error')

                self.label_delay.setText('inf')
                self.label_status.setText('disconnected')
                self.label_status.setStyleSheet("color:red;"); 
                QMessageBox.warning(self, "warning", f'{error}', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                

            if status == SEND_ERROR:
                context = args.get('context')
                error = args.get('error')
                QMessageBox.warning(self, "send fail", f'{context}\n{error}', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


    def send(self):
        self.editwidget.extract()
        message = self.editwidget.message

        # tochange
        address = '127.0.0.1'
        if self.radioButton_address.isChecked():
            address = self.lineEdit_address.text()
        protocol = self.comboBox_protocol.currentText()

        signal = {
            'type': SIGNAL_SEND,
            'context': message.to_json(),
            'dest': (address, LISTENING_PORT),
            'protocol': protocol
        }
        print(f'main   --> {message.to_json()}')
        self.work_thread.trigger_in.emit(signal)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = EdgelMainWindow()
    w.show()

    app.exec()
