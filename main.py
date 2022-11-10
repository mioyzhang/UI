#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMainWindow, QListWidgetItem

from ui.mainwindow import Ui_MainWindow
from ui.edit import Ui_Form
from widgets import NodeQListWidgetItem, MessageQListWidgetItem


class Node(object):

    def __init__(self, label=None, ip_address=None, mac_address=None):
        super(Node, self).__init__()
        self.label = label
        self.ip_address = ip_address
        self.mac_address = mac_address

        self.type = None
        self.status = None
        self.last_seen = None
        self.last_gps = None

    def __str__(self):
        return f'Node({self.label})'


class Message(object):
    def __init__(self, src=None, content=None):
        super(Message, self).__init__()
        self.src = src
        self.dst = None
        self.content = content
        self.gps = None
        self.time = None


class Logic(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def address_in_nodes(self, address):
        return address in [i.ip_address for i in self.nodes]


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

        try:
            while True:
                # 建立连接后，服务端等待客户端发送的数据，实现通信
                content = client.recv(1024).decode('utf-8')
                signal = {
                    'type': 'message',
                    'address': address,
                    'content': content
                }
                self.child_thread_trigger.emit(signal)
        except BaseException as e:
            print(e)

        finally:
            client.close()
            self.server.close()


class EditWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EditWidget, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow, Logic):
    main_thread_trigger = pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        Logic.__init__(self)

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

        self.pushButton_4.clicked.connect(self.p1_test)
        self.pushButton_3.clicked.connect(self.p2_test)
        self.listWidget_nodes.currentItemChanged.connect(self.display)
    
    def p1_test(self):
        src = '10.0.0.3'
        content = 'idosahgfiophdgiapohgiahgiapghi gjsigjsiog sg gjsg'
        print(src, content)
        m = Message(src=src, content=content)
        item = MessageQListWidgetItem(m)
        self.listWidget_messages.addItem(item)
        self.listWidget_messages.setItemWidget(item, item.widget)

    def p2_test(self):
        new_node = Node(label='s1', ip_address='10.0.0.1')
        self.add_node(new_node)

        item = NodeQListWidgetItem(new_node)
        item.setSizeHint(QSize(item.sizeHint().width(), 43))

        self.listWidget_nodes.addItem(item)
        self.listWidget_nodes.setItemWidget(item, item.widget)

    def display(self, *args):
        node = args[0].node
        self.label_29.setText(node.label)
        self.label_31.setText(node.ip_address)
        self.label_33.setText(node.type)
        self.label_35.setText(node.last_seen)
        self.label_37.setText(node.last_gps)

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
                new_node = Node(ip_address=ip_address)
                self.add_node(new_node)
                item = NodeQListWidgetItem(new_node)
                self.listWidget_nodes.addItem(item)
                self.listWidget_nodes.setItemWidget(item, item.widget)
        
        if date.get('type') == 'message':
            content = date.get('content')
            src = ip_address
            print(src, content)
            m = Message(src=src, content=content)
            item = MessageQListWidgetItem(m)
            self.listWidget_messages.addItem(item)
            self.listWidget_messages.setItemWidget(item, item.widget)
            
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    app.exec()
