import sys
import time
import json
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal

from ui.edgeWindow import Ui_EdgeMainWindow

from tools import *
from logic import Logic, Message, Packet
from transfer import TransferThread


class SocketThread(QThread):
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self, trigger):
        super(SocketThread, self).__init__()
        self.client = socket.socket()
        self.server = socket.socket()
        self.connected = None
        self.connections = []

        self.trigger = trigger
        self.trigger.connect(self.slot)

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
                        'status': PORT_MODIFY,
                        'port': self.connected[1]
                    }
                else:
                    back = {}
                return True, back

            else:
                print(f'disconnect {self.connected}')
                self.client.close()
                self.connected = None
                self.client = socket.socket()
        
        print(f'try to connect to {address}')
        try:
            self.client.connect(address)
            self.connected = address
            return True, {}
        
        except BaseException as e:
            back = {
                'status': CONNECT_FAIL,
                'error': str(e)
            }
            self.client = socket.socket()
            return False, back

    def check_delay(self, address):
        status, back1 = self.connect(address)
        if status:
            message_dict = {'type': 'test', 'time': time.time()}
            message = json.dumps(message_dict)
            status, back2 = self.send(message)

            if status:
                try:
                    recv = self.client.recv(2048).decode()
                    recv = json.loads(recv)

                    past_time = recv.get('time')
                    time.sleep(0.1)
                    delay = time.time() - past_time

                    print(past_time)
                    print(time.time())

                    back = {
                        'type': BACK_CHECK,
                        'status': CONNECT_SUCCESS,
                        'delay': delay
                    }

                    if back1.get('status') == PORT_MODIFY:
                        back['status'] = PORT_MODIFY
                        back['port'] = back1.get('port')

                    print(f'Thread  --> {back}')
                    self.trigger_out.emit(back)

                except BaseException as e:
                    back = {
                        'type': BACK_CHECK,
                        'status': RECV_ERROR,
                        'error': e
                    }
                    self.trigger_out.emit(back)
            else:
                back2['type'] = BACK_CHECK
                self.trigger_out.emit(back2)
        else:
            back1['type'] = BACK_CHECK
            self.trigger_out.emit(back1)
    
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
            address = args.get('address')
            self.check_delay(address)

        if type_ == SIGNAL_TEST:
            for i in range(5):
                print(i)
                time.sleep(1)

    def send(self, message):
        print(f'send {message} to {self.connected}')

        try:
            self.client.send(message.encode())
            back = {
                'status': SEND_SUCCESS,
                'context': message
            }
            return True, back
        except BaseException as e:
            back = {
                'status': SEND_ERROR,
                'context': message,
                'error': str(e)
            }
            print(f'fail send {message} to {self.connected}')

            self.client.close()
            self.client = socket.socket()
            return False, back

    def run(self):
        while True:
            time.sleep(1)
            print('.', end='')
        
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


class EdgeMainWindow(QMainWindow, Ui_EdgeMainWindow):
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
        self.pushButton_test2.clicked.connect(self.test)

        # self.editwidget.pushButton_submit.clicked.connect(self.send)
        self.pushButton_send.clicked.connect(self.send)

        self.pushButton_turn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # 子线程信号与槽
        # self.work_thread = SocketThread()
        # self.work_thread.trigger_in.connect(self.work_thread.slot)
        # self.work_thread.trigger_out.connect(self.slot)
        # self.work_thread.start()

        self.work_thread = SocketThread(self.main_thread_trigger)
        self.work_thread.trigger_in.connect(self.work_thread.slot)

        self.main_thread_trigger.connect(self.slot)
        # self.work_thread.trigger_out.connect(self.slot)
        self.work_thread.start()

    def test(self):
        # print('test')
        # for i in range(5):
        #     print(i)
        #     time.sleep(1)

        signal = {
            'type': SIGNAL_TEST,
            'address': (self.lineEdit_c_address.text(), int(self.lineEdit_c_port.text())),
        }
        print(f'main   --> {signal}')
        self.work_thread.trigger_in.emit(signal)

    def check_connect(self):
        self.pushButton_set.setChecked(False)
        self.lineEdit_c_address.setEnabled(False)
        self.lineEdit_c_port.setEnabled(False)

        signal = {
            'type': SIGNAL_CHECK,
            'address': (self.lineEdit_c_address.text(), int(self.lineEdit_c_port.text())),
        }
        print(f'main   --> {signal}')
        self.work_thread.trigger_in.emit(signal)
    
    def view_delay(self, delay):
        delay = delay * 10 ** 3 / 2
        self.label_delay.setText(f'{delay:.3f} ms')
        # self.label_delay.setText(f'{delay:.2e} ms')

        self.label_status.setText('connected')
        self.label_status.setStyleSheet("color:green;"); 

    def slot(self, args: dict):
        # if self.work_thread.started
        print(f'main   <-- {args}')
        type_ = args.get('type')

        if type_ == BACK_SEND:
            status = args.get('status')
            context = args.get('context')

        if type_ == BACK_CHECK:
            status = args.get('status')

            if status == PORT_MODIFY:
                port = args.get('port')
                self.lineEdit_c_port.setText(f'{port}')

            if status in [PORT_MODIFY, CONNECT_SUCCESS]:
                delay = args.get('delay')
                self.view_delay(delay)
            
            if status in [SEND_ERROR, RECV_ERROR, CONNECT_FAIL]:
                error = args.get('error')

                self.label_delay.setText('inf')
                self.label_status.setText('disconnect')
                self.label_status.setStyleSheet("color:red;")
                QMessageBox.warning(self, "warning", f'{error}', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

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

    w = EdgeMainWindow()
    w.show()

    app.exec()
