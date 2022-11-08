#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
Last edited: August 2017
"""

import sys
import socket

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMainWindow

from ui.mainwindow import Ui_MainWindow
from ui.edit import Ui_Form


class Node(object):

    def __init__(self, label=None, ip_address=None, mac_address=None):
        super(Node, self).__init__()
        self.label = label
        self.ip_address = ip_address
        self.mac_address = mac_address

        self.status = None

    def __str__(self):
        return f'Node({self.label})'


class Logic(object):
    def __init__(self):
        self.Nodes = []

    def add_node(self, node):
        if node not in self.Nodes:
            self.Nodes.append(node)

    def address_in_nodes(self, address):
        return address in [i.ip_address for i in self.Nodes]


class WorkThread(QThread):
    child_thread_trigger = pyqtSignal(dict)

    def __init__(self, trigger):
        super(WorkThread, self).__init__()
        self.main_thread_trigger = trigger
        self.server = socket.socket()

    def run(self):
        self.server.bind(('0.0.0.0', 8900))
        # 调用 listen() 方法开始监听端口， 传入的参数指定等待连接的最大数量
        self.server.listen(4)
        client, address = self.server.accept()
        signal = {
            'type': 'connect',
            'address': address
        }
        self.child_thread_trigger.emit(signal)

        while True:
            # 建立连接后，服务端等待客户端发送的数据，实现通信
            content = client.recv(1024).decode('utf-8')
            signal = {
                'type': 'message',
                'address': address,
                'content': content
            }
            self.child_thread_trigger.emit(signal)

        client.close()
        self.server.close()


class EditWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EditWidget, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow, Logic):
    main_thread_trigger = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.edit_widget = None
        self.setupUi(self)

        self.child_thread = WorkThread(self.main_thread_trigger)

        self.init_cnt()
        self.execute()

    def execute(self):
        self.child_thread.start()
        # 线程自定义信号连接的槽函数
        self.child_thread.child_thread_trigger.connect(self.message_process)

    def init_cnt(self):
        self.listWidget.currentRowChanged.connect(lambda x: self.stackedWidget.setCurrentIndex(x))

        self.action_2.triggered.connect(self.show_edit_widget)
        self.pushButton_2.clicked.connect(self.show_edit_widget)

    def show_edit_widget(self):
        self.edit_widget = EditWidget()
        self.edit_widget.show()

    def message_process(self, date: dict):
        # print(sys._getframe().f_code.co_name)
        # print(date)
        address = date.get('address')
        ip_address, port = address if address is not None else (None, None)
        if date.get('type') == 'connect':
            if self.address_in_nodes(ip_address):
                pass
            else:
                pass
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    app.exec()
