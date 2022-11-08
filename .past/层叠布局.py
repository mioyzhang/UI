import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉2要显示的内容", self)
        self.setStyleSheet("background-color:red;")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        self.stacked_layout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        self.setWindowTitle('First')
        self.setWindowIcon(QIcon('cat.png'))

        self.setFixedSize(300, 270)

        container = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")

        btn_press1 = QPushButton("抽屉1")
        btn_press2 = QPushButton("抽屉2")
        # 给按钮添加事件（即点击后要调用的函数）
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)

        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个Widget
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个Widget
        self.stacked_layout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
