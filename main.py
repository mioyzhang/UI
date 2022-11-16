#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket

import os
import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, \
    QMainWindow, QListWidgetItem, QFileDialog, QMessageBox

from ui.mainWindow import Ui_MainWindow
from ui.editForm import Ui_EditForm
from widgets import NodeQListWidgetItem, MessageQListWidgetItem

from tools import generate_random_gps
from logic import *


class WorkThread(QThread):
    child_thread_trigger = pyqtSignal(dict)

    def __init__(self, trigger):
        super(WorkThread, self).__init__()
        self.main_thread_trigger = trigger
        self.server = socket.socket()

    def run(self):

        # 调用 listen() 方法开始监听端口， 传入的参数指定等待连接的最大数量
        self.server.bind(('0.0.0.0', 8900))
        self.server.listen(32)

        # todo
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
            signal = {
                'type': 'error',
                'content': e
            }
            print(e)
            self.child_thread_trigger.emit(signal)

        finally:
            client.close()
            self.server.close()


class MainWindow(QMainWindow, Ui_MainWindow, Logic):
    main_thread_trigger = pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        Logic.__init__(self)

        self.child_thread = None
        self.edit_widget = None
        self.setupUi(self)

        # self.listWidget_files.hide()
        # self.listWidget_images.hide()
        self.listWidget_files.setHidden(True)
        self.listWidget_images.setHidden(True)

        self.init_cnt()
        self.execute()

    def execute(self):
        self.child_thread = WorkThread(self.main_thread_trigger)
        self.child_thread.start()
        # 线程自定义信号连接的槽函数
        self.child_thread.child_thread_trigger.connect(self.message_process)

    def init_cnt(self):
        self.listWidget.currentRowChanged.connect(lambda x: self.stackedWidget.setCurrentIndex(x))

        # self.action_2.triggered.connect(self.show_edit_widget)
        self.pushButton_reply.clicked.connect(self.turn_edit_widget)
        self.pushButton_cancel.clicked.connect(self.turn_view_widget)

        # listWidget双击删除
        self.listWidget_files.itemDoubleClicked['QListWidgetItem*'].connect(
            lambda: self.listWidget_files.takeItem(self.listWidget_files.currentRow()))
        self.listWidget_images.itemDoubleClicked['QListWidgetItem*'].connect(
            lambda: self.listWidget_images.takeItem(self.listWidget_images.currentRow()))

        self.toolButton_file.clicked.connect(self.choose_file)
        self.toolButton_img.clicked.connect(self.choose_image)

        self.pushButton_p1_test.clicked.connect(self.p1_test)
        self.pushButton_3.clicked.connect(self.p2_test)

        self.listWidget_nodes.currentItemChanged.connect(self.node_info_view)
        self.listWidget_messages.currentItemChanged.connect(self.message_info_view)
    
    def p1_test(self):

        message = {
            'sequence': 'l-232',
            'content': 'Hello world'
        }
        m = Message(args=message)
        p = Packet(message=m, src='192.168.0.156')
        print(m)
        print(p)

        item = MessageQListWidgetItem(p)
        self.listWidget_messages.addItem(item)
        self.listWidget_messages.setItemWidget(item, item.widget)

    def p2_test(self):
        new_node = Node(label='s1', ip_address='10.0.0.1')
        self.add_node(new_node)

        item = NodeQListWidgetItem(new_node)
        item.setSizeHint(QSize(item.sizeHint().width(), 43))

        self.listWidget_nodes.addItem(item)
        self.listWidget_nodes.setItemWidget(item, item.widget)

    def message_info_view(self, *args):
        packet = args[0].packet

        self.label_src.setText(packet.src)
        self.label_dst.setText(packet.dst)
        self.label_protocol.setText(packet.protocol)
        self.label_recv_time.setText(packet.recv_time)
        self.label_gps.setText(packet.message.gps)

    def node_info_view(self, *args):
        node = args[0].node
        self.label_29.setText(node.label)
        self.label_31.setText(node.ip_address)
        self.label_33.setText(node.type)
        self.label_35.setText(node.last_seen)
        self.label_37.setText(node.last_gps)

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
