import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from ui.edgeWindow import Ui_EdgeMainWindow

from tools import *
from logic import Message, Packet
from transfer import TransferThread
from widgets import MessageQListWidgetItem


class EdgeMainWindow(QMainWindow, Ui_EdgeMainWindow):

    def __init__(self):
        super().__init__()

        self.thread = None
        self.work_thread = None
        self.sequence = 0
        self.packets = []

        self.setupUi(self)
        self.init_connect()

        # temporary use
        self.editWidget.label_seq.setText(f'{self.sequence:0>8d}')

    def init_connect(self):

        self.pushButton_check.clicked.connect(self.check_connect)
        self.pushButton_test2.clicked.connect(self.test)

        # self.editWidget.pushButton_submit.clicked.connect(self.send)
        self.pushButton_send.clicked.connect(self.send)

        self.viewWidget.pushButton_cancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.editWidget.pushButton_cancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # fixme PyQt线程科学用法
        self.thread = QThread()
        self.work_thread = TransferThread()
        self.work_thread.moveToThread(self.thread)
        self.work_thread.trigger_in.connect(self.work_thread.slot)
        self.work_thread.trigger_out.connect(self.slot)
        self.thread.start()

    def test(self):
        print('test')

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
        self.label_status.setStyleSheet("color:green;")

    def add_packet(self, packet):
        print(f'add {packet}')
        if packet in self.packets:
            return
        self.packets.append(packet)
        item = MessageQListWidgetItem(packet)
        self.listWidget_msgs.addItem(item)
        self.listWidget_msgs.setItemWidget(item, item.widget)

    def slot(self, args: dict):
        # if self.work_thread.started
        print(f'main   <-- {args}')
        type_ = args.get('type')
        status = args.get('status')

        if type_ == OUT_SEND:
            if status == SEND_SUCCESS:
                content = args.get('content')
                ip_address = args.get('ip_address')
                flow = args.get('flow')
                send_time = args.get('send_time')
                message = Message(content)
                packet = Packet(message=message, dst=ip_address, flow=flow, send_time=send_time)
                self.add_packet(packet)
            
            else:
                content = args.get('content')
                error = args.get('error')
                QMessageBox.warning(self, "warning", f'{content}\n{error}', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if type_ == OUT_ERROR:
            if status in [SEND_ERROR, RECV_ERROR, TEST_DELAY_FAIL]:
                error = args.get('error')
                self.label_delay.setText('inf')
                self.label_status.setText('disconnect')
                self.label_status.setStyleSheet("color:red;")
                QMessageBox.warning(self, "warning", f'{error}', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if type_ == OUT_INFO:
            if status == TEST_DELAY:
                delay = args.get('delay')
                self.view_delay(delay)

    def send(self):
        self.editWidget.extract()
        message = self.editWidget.message

        # tochange
        address = '127.0.0.1'
        if self.radioButton_address.isChecked():
            address = self.lineEdit_address.text()
        protocol = self.comboBox_protocol.currentText()

        signal = {
            'type': SIGNAL_SEND,
            'content': message.to_json(),
            'dest': (address, LISTENING_PORT),
            'protocol': protocol
        }
        print(f'main   --> {message}')
        self.work_thread.trigger_in.emit(signal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = EdgeMainWindow()
    w.show()
    app.exec()
