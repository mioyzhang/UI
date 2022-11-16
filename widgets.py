import os
import sys
import typing

from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

import resouce_rc
from ui.editForm import Ui_EditForm
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
        self.label_3.setText(self.node.ip_address)
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

        self.label_2.setText(self.packet.src)
        self.label_3.setText(str(self.packet.message))

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
            'type': self.comboBox_msg_type.currentText(),
            'with_gps': self.radioButton_gps.isChecked(),
            'gps': self.lineEdit_gps.text(),
            'content': self.textEdit.toPlainText(),
            'files': [self.listWidget_files.item(i).text() for i in range(self.listWidget_files.count())],
            'images': [self.listWidget_images.item(i).text() for i in range(self.listWidget_images.count())]

        }
        self.message = Message(info)
        print(self.message)


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
    w = MessageEditWidget()
    w.show()

    app.exec()
