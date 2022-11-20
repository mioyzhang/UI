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
from ui.testWidgets import Ui_Form

from tools import generate_random_gps
from logic import *


class NodeQListWidgetItem(QListWidgetItem):
    def __init__(self, node):
        super().__init__()

        self.node = node
        
        self.widget = QWidget()
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.widget)
        self.label.setMaximumSize(QSize(41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(":/icon/icon/cat.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.label_2.setText(self.node.label)
        self.label_3.setText(f'{self.node.ip_address}:{self.node.port}')
        self.pushButton.setText("测试连接")
        self.pushButton_2.setText("发送消息")

        self.setSizeHint(self.widget.sizeHint())


class MessageQListWidgetItem(QListWidgetItem):
    def __init__(self, packet):
        super().__init__()
        self.packet = packet
        self.init_ui()
    
    def init_ui(self):
        self.widget = QWidget()
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_1 = QLabel(self.widget)
        self.label_1.setMaximumSize(QSize(41, 41))
        self.label_1.setPixmap(QPixmap(":/icon/icon/无人机.png"))
        self.label_1.setScaledContents(True)

        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        spacerItem2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacerItem3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacerItem4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.label_2 = QLabel(self.widget)
        self.label_3 = QLabel(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout.addItem(spacerItem4)

        self.horizontalLayout.addWidget(self.label_1)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_2.setText(f'{self.packet.src}')
        self.label_3.setText(self.packet.message.summary())

        # self.widget.setMaximumHeight(81)
        self.setSizeHint(self.widget.sizeHint())


class MessageEditWidget(QWidget, Ui_EditForm): 
    # def __init__(self, parent: typing.Optional['QWidget'] = ...) -> None:
    #     super().__init__(parent)
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

        self.pushButton_submit.clicked.connect(self.extract)
        self.pushButton_generate_msg.clicked.connect(self.generate_msg)

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
        print(self.message)

    def clear_info(self):
        self.label_seq.setText('')
        self.comboBox_msg_type.setCurrentIndex(0)
        self.radioButton_gps.setChecked(False)
        self.lineEdit_gps.setText('')
        self.textEdit.setPlainText(''),
        self.listWidget_files.clear()
        self.listWidget_images.clear()

    def generate_msg(self):
        self.clear_info()
        import faker
        faker = faker.Faker()

        # img_path = '/home/dell/workspace/UI/resource/icon'
        img_path = 'D:/Develop/PycharmProjects/UI/resource/icon'
        imgs = os.listdir(img_path)
        imgs = random.sample(imgs, random.randint(0, len(imgs)))
        imgs = [os.path.join(img_path, i) for i in imgs]

        file_path = '/home/dell/workspace/UI/resource/file'
        file_path = 'D:/Develop/PycharmProjects/UI/resource/file'
        files = os.listdir(file_path)
        files = random.sample(files, random.randint(0, len(files)))
        files = [os.path.join(file_path, i) for i in files]

        info = {
            'sequence': random.randint(0, 10000),
            'type': random.randint(0, 3),
            'with_gps': random.choice([True, False]),
            'gps': generate_random_gps(),
            'content': faker.text(),
            'files': files,
            'images': imgs
        }

        self.label_seq.setText(f"{info.get('sequence')}")
        self.comboBox_msg_type.setCurrentIndex(info.get('type'))
        self.radioButton_gps.setChecked(info.get('with_gps'))
        self.lineEdit_gps.setText(f"{info.get('gps')}")
        self.textEdit.setPlainText(info.get('content')),
        self.listWidget_files.addItems(info.get('files'))
        self.listWidget_images.addItems(info.get('images'))

        if info.get('files'):
            self.listWidget_files.show()
        if info.get('images'):
            self.listWidget_images.show()


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
        save_path = 'D:/Develop/PycharmProjects/UI/resource'
        if images:
            self.scrollArea.show()
            for i in images:
                img_path = os.path.join(save_path, i)
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
        img_path = 'D:/Develop/PycharmProjects/UI/resource/icon'
        imgs = [os.path.join(img_path, i) for i in os.listdir(img_path)]

        verticalLayout_images = QVBoxLayout(self.scrollAreaWidgetContents)
        for i in imgs:
            label = QLabel(self.scrollAreaWidgetContents)
            label.setPixmap(QPixmap(i))
            verticalLayout_images.addWidget(label)


class TestWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        # t = T1('33', 'gfsgsgds')
        # item = MessageQListWidgetItem(t)
        # self.listWidget.addItem(item)
        # self.listWidget.setItemWidget(item, item.widget)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # w = TestWindow()
    # w = MessageEditWidget()
    w = MessageViewWidget()
    w.show()

    app.exec()
