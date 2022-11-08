import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('First')
        self.setWindowIcon(QIcon('cat.png'))

        container = QVBoxLayout()

        form_layout = QFormLayout()

        # 创建1个输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入账号")
        form_layout.addRow("账号：", edit)

        # 创建另外1个输入框
        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        form_layout.addRow("密码：", edit2)

        container.addLayout(form_layout)

        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100, 30)

        container.addWidget(login_btn, alignment=Qt.AlignRight)
        self.setLayout(container)

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
