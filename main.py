#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket

import os
import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMainWindow, QListWidgetItem, QFileDialog

from ui.mainwindow import Ui_MainWindow
from ui.edit import Ui_EditForm
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


class EditWidget(QWidget, Ui_EditForm):
    message = None

    def __init__(self):
        super(EditWidget, self).__init__()
        self.setupUi(self)

        self.listWidget_files.hide()
        self.listWidget_images.hide()

        self.setWindowIcon(QIcon('resource/icon/cat.png'))
        self.init_connect()

    def init_connect(self):
        self.pushButton_position.clicked.connect(self.generate_random_gps)
        self.pushButton_generate.clicked.connect(self.generate_random_gps)
        self.pushButton_submit.clicked.connect(self.extract)

        self.toolButton_file.clicked.connect(self.choose_file)
        self.toolButton_img.clicked.connect(self.choose_image)

        self.listWidget_files.itemDoubleClicked['QListWidgetItem*'].connect(lambda: self.listWidget_files.takeItem(self.listWidget_files.currentRow()))
        self.listWidget_images.itemDoubleClicked['QListWidgetItem*'].connect(lambda: self.listWidget_images.takeItem(self.listWidget_images.currentRow()))

    def generate_random_gps(self):
        longitude, latitude = generate_random_gps()
        self.lineEdit.setText(f'{longitude}, {latitude}')

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
        print(self.message)


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
        content = 'Hello world'
        print(src, content)
        m = Message(content=content)
        p = Packet(src=src, dst=None, message=m)
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

            m = Message(content=content)
            p = Packet(src=src, dst=None, message=m)

            item = MessageQListWidgetItem(p)
            self.listWidget_messages.addItem(item)
            self.listWidget_messages.setItemWidget(item, item.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    app.exec()
