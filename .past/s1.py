import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('First')
    w.setWindowIcon(QIcon('../resource/icon/cat.png'))

    label = QLabel('信息', w)
    label.setGeometry(20, 20, 30, 20)

    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入')
    edit.setGeometry(50, 20, 200, 20)

    btn = QPushButton('test', w)
    btn.setGeometry(50, 80, 30, 30)

    w.resize(300, 300)
    w.move(0, 0)

    # center_pointer = QDesktopWidget().availableGeometry().center()
    # print(center_pointer)
    # x = center_pointer.x()
    # y = center_pointer.y()
    # s = w.frameGeometry().getRect()
    # w.move(int(x - s[2] / 2), int(y - s[3] / 2))

    w.show()
    app.exec_()
