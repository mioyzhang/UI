import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 300)
        self.setWindowTitle('First')
        self.setWindowIcon(QIcon('cat.png'))

        container = QVBoxLayout()

        hobby_box = QGroupBox("爱好")
        v_layout = QVBoxLayout()
        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("烫头")

        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        gender_box = QGroupBox("性别")
        h_layout = QHBoxLayout()
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        gender_box.setLayout(h_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
