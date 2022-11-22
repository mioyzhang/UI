#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, \
    QMainWindow, QListWidgetItem, QFileDialog, QMessageBox

from ui.mainWindow import Ui_MainWindow
from widgets import NodeQListWidgetItem, MessageQListWidgetItem

from logic import *
from tools import *
from transfer import TransferThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.sequence = random.randint(0, 10 ** 8 - 1)
        self.nodes = []
        self.messages = []
        self.packets = []

        self.thread1 = None
        self.thread2 = None
        self.recv_thread = None
        self.send_thread = None
        self.setupUi(self)

        self.init_cnt()
        self.editWidget.label_seq.setText(f'{self.sequence:0>8d}')

    def init_cnt(self):
        self.listWidget.currentRowChanged.connect(lambda x: self.stackedWidget.setCurrentIndex(x))

        self.listWidget_nodes.currentItemChanged.connect(self.node_info_view)
        self.listWidget_messages.currentItemChanged.connect(self.message_info_view)

        # editWidget
        self.editWidget.pushButton_cancel.clicked.connect(self.turn_view_widget)
        self.editWidget.pushButton_generate_msg.clicked.connect(self.generate_msg)
        self.editWidget.pushButton_clear.clicked.connect(self.editWidget.clear_info)
        # self.editWidget.pushButton_submit.clicked.connect(self.editWidget.extract)

        self.pushButton_send.clicked.connect(self.send_message)
        self.pushButton_test2.clicked.connect(self.p1_test)

        self.pushButton_p2_test.clicked.connect(self.p2_test)

        self.viewWidget.pushButton_cancel.clicked.connect(self.turn_edit_widget)

        # 子线程初始化
        self.thread1 = QThread()

        self.recv_thread = TransferThread(udp_port=LISTENING_PORT_1)
        self.recv_thread.moveToThread(self.thread1)
        self.recv_thread.trigger_start.connect(self.recv_thread.udp_accept)
        self.recv_thread.trigger_out.connect(self.slot)
        # self.recv_thread.trigger_in.connect(self.recv_thread.slot)

        self.thread1.start()
        self.recv_thread.trigger_start.emit()

        self.thread2 = QThread()
        self.send_thread = TransferThread()
        self.send_thread.moveToThread(self.thread2)
        self.send_thread.trigger_in.connect(self.send_thread.slot)
        self.send_thread.trigger_out.connect(self.slot)
        self.thread2.start()

    def generate_msg(self):
        self.editWidget.generate_msg()
        self.editWidget.label_seq.setText(f'{self.sequence:0>8d}')

    def send_message(self):
        self.editWidget.extract()
        message = self.editWidget.message
        protocol = self.comboBox_protocol.currentText()

        if self.radioButton_address.isChecked():
            address = extract_address(self.lineEdit_address.text())
            if not address:
                QMessageBox.warning(self, "warning", f'请输入正确ip地址', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                return

        else:
            index = self.comboBox_dst.currentIndex()
            if index == -1:
                QMessageBox.warning(self, "warning", f'请选择节点', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                return
            node = self.nodes[index]
            ip = node.ip_address
            port = node.port if node.port else LISTENING_PORT
            address = (ip, port)

        print(f'send {message} to {address}')

        signal = {
            'type': SIGNAL_SEND,
            'content': message.to_json(),
            'dest': address,
            'protocol': protocol
        }
        self.send_thread.trigger_in.emit(signal)
        self.sequence += 1

    def slot(self, args):
        print(f'main <-- {args}')
        type_ = args.get('type')
        status = args.get('status')

        if type_ == OUT_ERROR:
            # signal 2
            error = args.get('error')
            QMessageBox.warning(self, "warning", f'{error}', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if type_ == OUT_INFO:
            # signal 1
            if status == INIT_ACCEPT_SUCCESS:
                port = args.get('port')
                self.statusBar().showMessage(f'Listening on port {port}', 5000)

            # signal 3
            if status == OTHER_TEST_DELAY:
                hostname = args.get('hostname')
                ip_address = args.get('ip_address')
                recv_time = args.get('recv_time')
                new_node = Node(label=hostname, ip_address=ip_address, last_seen=recv_time)
                self.add_node(new_node)

            # signal 4
            if status == OTHER_TEST_DELAY:
                pass

            if status == RECV_CONNECTION:
                ip_address = args.get('ip_address')
                port = args.get('port')
                print(f'{ip_address}:{port} connect')

            if status == TEST_DELAY:
                label = args.get('hostname') if args.get('hostname') else args.get('ip_address')
                ip_address = args.get('ip_address')
                port = args.get('port')
                node = Node(label=label, ip_address=ip_address, port=port)
                self.add_node(node)

        if type_ == OUT_RECV:
            ip_address = args.get('ip_address')
            content = args.get('content')
            recv_time = args.get('recv_time')
            flow = args.get('flow')

            message = Message(content)
            packet = Packet(src=ip_address, message=message, recv_time=recv_time)
            self.add_packet(packet)

        if type_ == OUT_SEND:
            if status == SEND_SUCCESS:
                content = args.get('content')
                ip_address = args.get('ip_address')
                flow = args.get('flow')
                send_time = args.get('send_time')
                message = Message(content)
                packet = Packet(message=message, dst=ip_address, flow=flow, send_time=send_time)
                self.add_packet(packet)

        pass

    def p1_test(self):

        message = {
            'sequence': 'l-232',
            'content': 'Hello world'
        }
        m = Message(args=message)
        p = Packet(message=m, src='192.168.0.156')

        item = MessageQListWidgetItem(p)
        self.listWidget_messages.addItem(item)
        self.listWidget_messages.setItemWidget(item, item.widget)

    def p2_test(self):
        new_node = Node(generate=True)
        self.add_node(new_node)

    def add_node(self, node: Node):

        if node in self.nodes:
            index = self.nodes.index(node)
            self.nodes[index].update(node)
        else:
            self.nodes.append(node)
            item = NodeQListWidgetItem(node)
            item.setSizeHint(QSize(item.sizeHint().width(), 43))
            self.listWidget_nodes.addItem(item)
            self.listWidget_nodes.setItemWidget(item, item.widget)

            self.comboBox_dst.addItem(str(node))
            self.comboBox_dst.setCurrentIndex(-1)

    def add_packet(self, packet):
        print(f'add {packet}')
        if packet in self.packets:
            return
        self.packets.append(packet)
        item = MessageQListWidgetItem(packet)
        self.listWidget_messages.addItem(item)
        self.listWidget_messages.setItemWidget(item, item.widget)

    def message_info_view(self, *args):
        self.stackedWidget_message.setCurrentIndex(0)
        packet = args[0].packet
        self.viewWidget.display(packet.message)

        self.label_src.setText(f'{packet.src}')
        self.label_dst.setText(f'{packet.dst}')
        self.label_protocol.setText(f'{packet.protocol}')
        self.label_recv_time.setText(f'{packet.recv_time}')
        self.label_gps.setText(f'{packet.message.gps}')

    def node_info_view(self, *args):
        node = args[0].node
        self.label_d_label.setText(node.label)
        self.label_d_ip.setText(node.ip_address)
        self.label_d_type.setText(NODE_TYPE[node.type])
        self.label_d_time.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(node.last_seen)))

    def turn_view_widget(self):
        self.stackedWidget_message.setCurrentIndex(0)

    def turn_edit_widget(self):
        self.stackedWidget_message.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
