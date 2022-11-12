import sys

from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

import resouce_rc
from ui.testwidgets import Ui_Form


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
    def __init__(self, message):
        super().__init__()
        self.message = message 
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

        self.label_2.setText(self.message.src)
        self.label_3.setText(self.message.message.content)

        # self.widget.setMaximumHeight(81)

        self.setSizeHint(self.widget.sizeHint())


class T1(object):
    def __init__(self, src=None, content=None):
        super().__init__()
        self.src = src
        self.content = content


class TestWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        t = T1('33', 'gfsgsgds')
        item = MessageQListWidgetItem(t)
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item.widget)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TestWindow()
    w.show()

    app.exec()
