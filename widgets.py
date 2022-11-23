import os
import sys
import random
import typing

from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import resouce_rc
from ui.editForm import Ui_EditForm
from ui.viewForm import Ui_ViewForm
from ui.test import Ui_Form

from logic import *


class MessageEditWidget(QWidget, Ui_EditForm): 
    def __init__(self, *args) -> None:
        super().__init__(*args)

        self.message = None
        self.setupUi(self)
        self.listWidget_files.hide()
        self.listWidget_images.hide()
        self.init_slot()

    def init_slot(self):
        self.pushButton_position.clicked.connect(self.generate_random_gps)
        self.pushButton_generate.clicked.connect(self.generate_random_gps)

        # self.pushButton_cancel.clicked.connect()
        self.pushButton_clear.clicked.connect(self.clear_info)
        self.pushButton_generate_msg.clicked.connect(self.generate_msg)
        # self.pushButton_submit.clicked.connect(self.extract)

        self.toolButton_file.clicked.connect(self.choose_file)
        self.toolButton_img.clicked.connect(self.choose_image)

        self.listWidget_files.itemDoubleClicked['QListWidgetItem*'].connect(
            lambda: self.listWidget_files.takeItem(self.listWidget_files.currentRow()))
        self.listWidget_images.itemDoubleClicked['QListWidgetItem*'].connect(
            lambda: self.listWidget_images.takeItem(self.listWidget_images.currentRow()))

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
        image_names = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), image_filter)
        image_names = image_names[0]
        self.listWidget_images.show()
        for i in image_names:
            self.listWidget_images.addItem(i)
        print(image_names)

    def extract(self):
        info = {
            'sequence': self.label_seq.text(),
            'type': self.comboBox_msg_type.currentIndex(),
            'with_gps': self.radioButton_gps.isChecked(),
            'gps': self.lineEdit_gps.text(),
            'content': self.textEdit.toPlainText(),
            'files': [self.listWidget_files.item(i).text() for i in range(self.listWidget_files.count())],
            'images': [self.listWidget_images.item(i).text() for i in range(self.listWidget_images.count())]
        }
        self.message = Message(info)

    def clear_info(self):
        # self.label_seq.setText('')
        self.comboBox_msg_type.setCurrentIndex(0)
        self.radioButton_gps.setChecked(False)
        self.lineEdit_gps.setText('')
        self.textEdit.setPlainText(''),
        self.listWidget_files.clear()
        self.listWidget_images.clear()
    
    def display_message(self, message: Message):

        self.label_seq.setText(f"{message.sequence}")
        self.comboBox_msg_type.setCurrentIndex(message.type)
        self.radioButton_gps.setChecked(message.with_gps)
        self.lineEdit_gps.setText(f'{message.gps}')
        self.textEdit.setPlainText(message.content),
        self.listWidget_files.addItems(message.files)
        self.listWidget_images.addItems(message.images)

        if message.files:
            self.listWidget_files.show()
        if message.images:
            self.listWidget_images.show()

    def generate_msg(self):
        self.clear_info()
        message = Message(None)
        self.display_message(message)


class MessageViewWidget(QWidget, Ui_ViewForm):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.setupUi(self)
        self.scrollArea.hide()
        # self.show_img()
        self.layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.pushButton_test1.clicked.connect(self.test)
        self.pushButton_test2.clicked.connect(self.clear)

    def clear(self):
        self.label_seq.clear()
        self.label_type.clear()
        self.label_gps.clear()
        self.textBrowser.clear()
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().deleteLater()

    def display(self, message):
        self.clear()
        self.label_seq.setText(f'{message.sequence}')
        self.label_type.setText(f'{message.type}')
        self.label_gps.setText(f'{message.gps}')
        self.textBrowser.setPlainText(f'{message.content}')
        images = message.images
        if images:
            self.scrollArea.show()
            for i in images:
                img_path = os.path.join(SAVE_PATH, i)
                label = QLabel(self.scrollAreaWidgetContents)
                label.setPixmap(QPixmap(img_path))
                self.layout.addWidget(label)

    def test(self):
        message = {
            'sequence': 'l-232',
            'content': 'Hello world'
        }
        m = Message(args=message)
        p = Packet(message=m, src='192.168.0.156')
        self.display(m)

    def show_img(self):
        imgs = [os.path.join(IMG_PATH, i) for i in os.listdir(IMG_PATH)]

        verticalLayout_images = QVBoxLayout(self.scrollAreaWidgetContents)
        for i in imgs:
            label = QLabel(self.scrollAreaWidgetContents)
            label.setPixmap(QPixmap(i))
            verticalLayout_images.addWidget(label)


class NodeQListWidgetItem(QListWidgetItem):
    def __init__(self, node: Node):
        super().__init__()

        self.node = node
        self.widget = QWidget()
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_icon = QLabel(self.widget)
        self.label_label = QLabel(self.widget)
        self.label_ip = QLabel(self.widget)
        self.label_delay = QLabel(self.widget)
        self.pushButton_test = QPushButton(self.widget)
        self.pushButton_send = QPushButton(self.widget)

        self.label_icon.setMaximumSize(QSize(41, 41))
        self.label_icon.setPixmap(QPixmap(":/icon/icon/node.png"))
        self.label_icon.setScaledContents(True)

        spacerItem0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem4 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addWidget(self.label_icon)
        self.horizontalLayout.addItem(spacerItem0)
        self.horizontalLayout.addWidget(self.label_label)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.label_ip)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.label_delay)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.pushButton_test)
        self.horizontalLayout.addWidget(self.pushButton_send)
        self.horizontalLayout.addItem(spacerItem4)

        self.pushButton_test.setText("测试连接")
        self.pushButton_send.setText("发送消息")
        self.label_delay.setText('inf')
        # self.label_delay.setStyleSheet("color:yellow;")

        self.setSizeHint(self.widget.sizeHint())
        self.view()

    def view(self):
        icons = [
            QPixmap(":/icon/icon/node.png"),
            QPixmap(":/icon/icon/服务器.png"),
            QPixmap(":/icon/icon/射手.png"),
            QPixmap(":/icon/icon/传感器.png"),
            QPixmap(":/icon/icon/无人机.png"),
            QPixmap(":/icon/icon/飞机.png"),
            QPixmap(":/icon/icon/皮卡 (1).png"),
            QPixmap(":/icon/icon/轮船.png"),
        ]

        self.label_icon.setPixmap(icons[self.node.type])
        self.label_label.setText(self.node.label)
        self.label_ip.setText(self.node.ip_address)


class MessageQListWidgetItem(QListWidgetItem):
    def __init__(self, packet: Packet):
        super().__init__()
        self.packet = packet

        self.widget = QWidget()
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_icon = QLabel(self.widget)
        self.label_icon.setMaximumSize(QSize(41, 41))
        self.label_icon.setPixmap(QPixmap(":/icon/icon/node.png"))
        self.label_icon.setScaledContents(True)
        
        self.label_label = QLabel(self.widget)
        self.label_content = QLabel(self.widget)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.label_icon_img = QLabel(self.widget)
        self.label_icon_img.setMaximumSize(QSize(15, 15))
        self.label_icon_img.setPixmap(QPixmap(":/icon/icon/图像.png"))
        self.label_icon_img.setScaledContents(True)

        self.label_icon.setMaximumSize(QSize(41, 41))
        self.label_icon_file = QLabel(self.widget)
        self.label_icon_file.setMaximumSize(QSize(15, 15))
        self.label_icon_file.setPixmap(QPixmap(":/icon/icon/文件.png"))
        self.label_icon_file.setScaledContents(True)

        self.horizontalLayout_other = QHBoxLayout()
        self.horizontalLayout_other.addItem(spacerItem)
        self.horizontalLayout_other.addWidget(self.label_icon_img)
        self.horizontalLayout_other.addWidget(self.label_icon_file)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.label_label)
        self.verticalLayout.addWidget(self.label_content)
        self.verticalLayout.addLayout(self.horizontalLayout_other)

        self.horizontalLayout.addWidget(self.label_icon)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.setSizeHint(self.widget.sizeHint())
        self.view()

    def view(self):
        icons = [
            QPixmap(":/icon/icon/node.png"),
            QPixmap(":/icon/icon/服务器.png"),
            QPixmap(":/icon/icon/射手.png"),
            QPixmap(":/icon/icon/传感器.png"),
            QPixmap(":/icon/icon/无人机.png"),
            QPixmap(":/icon/icon/飞机.png"),
            QPixmap(":/icon/icon/皮卡 (1).png"),
            QPixmap(":/icon/icon/轮船.png"),
        ]

        # self.label_icon.setPixmap(icons[self.node.type])
        # self.label_label.setText(self.node.label)
        # self.label_ip.setText(self.node.ip_address)
        self.label_content.setText(self.packet.message.summary())


class TestWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        # t = Node(generate=True)
        # item = NodeQListWidgetItem(t)
        # item.setSizeHint(QSize(item.sizeHint().width(), 43))
        # self.listWidget.addItem(item)
        # self.listWidget.setItemWidget(item, item.widget)

        t = Message()
        p = Packet(message=t)
        item = MessageQListWidgetItem(t)
        item.setSizeHint(QSize(item.sizeHint().width(), 43))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item.widget)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TestWindow()
    # w = MessageEditWidget()
    # w = MessageViewWidget()
    w.show()

    app.exec()
