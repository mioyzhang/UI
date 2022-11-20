#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
from math import ceil
from threading import Thread

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, \
    QMainWindow, QListWidgetItem, QFileDialog, QMessageBox

from ui.mainWindow import Ui_MainWindow
from widgets import NodeQListWidgetItem, MessageQListWidgetItem

from logic import *


class WorkThread(QObject):
    trigger_start = pyqtSignal()
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self):
        super(WorkThread, self).__init__()
        self.server = socket.socket()

    def slot(self, args):
        pass

    def recv_process(self, client, addr):
        try:
            while True:
                content = client.recv(BUFFER_SIZE).decode('utf-8')
                if not content:
                    print(f'{addr} disconnect')
                    client.close()
                    break

                info = json.loads(content)
                print(f'recv: {info}')

                if not isinstance(info, dict):
                    print(info)
                    continue

                type_ = info.get('type')
                if type_ == PACKET_TEST:
                    print(f'{addr} recv {content}')
                    client.send(content.encode())

                if type_ in [PACKET_NONE, PACKET_DETECT, PACKET_ORDER, PACKET_REPLY]:

                    signal = {
                        'type': OUT_RECV,
                        'content': info,
                        'ip_address': addr[0],
                        'port': addr[1],
                        'flow': RX,
                        'recv_time': time.time()
                    }
                    self.trigger_out.emit(signal)

                if type_ == PACKET_FILE:
                    client.send('ready'.encode())
                    file_name = info.get('file_name')
                    file_size = info.get('file_size')
                    file_path = os.path.join(save_path, file_name)
                    print(f'recv {file_name} {file_size} byte')

                    with open(file_path, 'wb') as f:
                        for i in range(ceil(file_size / BUFFER_SIZE)):
                            bytes_read = client.recv(BUFFER_SIZE)
                            if not bytes_read:
                                break
                            f.write(bytes_read)

                    print(f'recv {file_name}')
                    client.send('finish'.encode())
        except BaseException as e:
            print(e)
            raise e

    def accept(self):
        try:
            self.server.bind(('0.0.0.0', LISTENING_PORT))
            self.server.listen(32)
            print(f'Listening on port {LISTENING_PORT}')

            signal = {
                'type': OUT_INFO,
                'status': INIT_SUCCESS,
                'port': LISTENING_PORT
            }
            self.trigger_out.emit(signal)

            # todo

            self.server.settimeout(None)
            while True:
                client, address = self.server.accept()
                client.settimeout(None)
                print(f'recv connect from {address}')
                signal = {
                    'type': OUT_INFO,
                    'status': RECV_CONNECTION,
                    'ip_address': address[0],
                    'port': address[1],
                }
                self.trigger_out.emit(signal)
                # self.recv_process(client, address)
                t = Thread(target=self.recv_process, args=(client, address))
                t.start()
                t.join()

        except BaseException as e:
            signal = {
                'type': OUT_ERROR,
                'error': e
            }
            self.trigger_out.emit(signal)
            raise e

        finally:
            self.server.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    main_thread_trigger = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.nodes = []
        self.messages = []
        self.packets = []

        self.thread = None
        self.work_thread = None
        self.setupUi(self)

        self.init_cnt()

    def init_cnt(self):
        self.listWidget.currentRowChanged.connect(lambda x: self.stackedWidget.setCurrentIndex(x))

        # self.action_2.triggered.connect(self.show_edit_widget)
        # self.pushButton_reply.clicked.connect(self.turn_edit_widget)
        self.viewwidget.pushButton_cancel.clicked.connect(self.turn_edit_widget)

        self.pushButton_test2.clicked.connect(self.p1_test)
        self.pushButton_3.clicked.connect(self.p2_test)

        self.listWidget_nodes.currentItemChanged.connect(self.node_info_view)
        self.listWidget_messages.currentItemChanged.connect(self.message_info_view)

        # 子线程初始化
        self.thread = QThread()
        self.work_thread = WorkThread()
        self.work_thread.moveToThread(self.thread)

        self.work_thread.trigger_start.connect(self.work_thread.accept)
        self.work_thread.trigger_in.connect(self.work_thread.slot)
        self.work_thread.trigger_out.connect(self.slot)

        self.thread.start()
        self.work_thread.trigger_start.emit()

    def slot(self, args) -> None:
        print(f'main <-- {args}')
        type_ = args.get('type')
        status = args.get('status')

        if type_ == OUT_ERROR:
            error = args.get('error')
            QMessageBox.warning(self, "warning", f'{error}', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)

        if type_ == OUT_INFO:
            if status == INIT_SUCCESS:
                port = args.get('port')
                self.statusBar().showMessage(f'Listening on port {port}')

            if status == RECV_CONNECTION:
                label = args.get('label') if args.get('label') else args.get('ip_address')
                ip_address = args.get('ip_address')
                port = args.get('port')
                node = Node(label=label, ip_address=ip_address, port=port)
                self.add_node(node)

        if type_ == OUT_RECV:
            ip_address = args.get('ip_address')
            port = args.get('port')
            content = args.get('content')
            recv_time = args.get('recv_time')
            message = Message(content)
            packet = Packet(src=(ip_address, port), message=message, recv_time=recv_time)
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
        new_node = Node(label='s1', ip_address='10.0.0.1', port=1234)
        self.add_node(new_node)

    def add_node(self, node: Node):
        if node in self.nodes:
            return

        self.nodes.append(Node)
        item = NodeQListWidgetItem(node)
        item.setSizeHint(QSize(item.sizeHint().width(), 43))
        self.listWidget_nodes.addItem(item)
        self.listWidget_nodes.setItemWidget(item, item.widget)

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
        self.viewwidget.display(packet.message)

        self.label_src.setText(f'{packet.src}')
        self.label_dst.setText(f'{packet.dst}')
        self.label_protocol.setText(f'{packet.protocol}')
        self.label_recv_time.setText(f'{packet.recv_time}')
        self.label_gps.setText(f'{packet.message.gps}')

    def node_info_view(self, *args):
        node = args[0].node
        self.label_29.setText(node.label)
        self.label_31.setText(node.ip_address)
        self.label_33.setText(node.type)
        self.label_35.setText(node.last_seen)
        self.label_37.setText(node.last_gps)

    def turn_view_widget(self):
        self.stackedWidget_message.setCurrentIndex(0)

    def turn_edit_widget(self):
        self.stackedWidget_message.setCurrentIndex(1)

    def message_process(self, signal: dict):
        # print(sys._getframe().f_code.co_name)
        print(f'Main recv {signal}')
        ip_address, port = signal.get('address')
        type_ = signal.get('type')

        if type_ == 'connect':
            if self.address_in_nodes(ip_address):
                pass
            else:
                new_node = Node(ip_address=ip_address)
                self.add_node(new_node)
                item = NodeQListWidgetItem(new_node)
                self.listWidget_nodes.addItem(item)
                # todo
                self.listWidget_nodes.setItemWidget(item, item.widget)
        
        if type_ == 'message':
            content = signal.get('content')
            message = {
                'content': content
            }
            m = Message(args=message)
            p = Packet(message=m, src=ip_address)

            item = MessageQListWidgetItem(p)
            self.listWidget_messages.addItem(item)
            self.listWidget_messages.setItemWidget(item, item.widget)

        if type_ == 'error':
            content = signal.get('content')
            QMessageBox.warning(self, content, QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    app.exec()
