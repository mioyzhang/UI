from PyQt5.Qt import QApplication, QWidget, QPushButton, QThread, QMutex, pyqtSignal
import sys
import time



class PreventFastClickThreadSignal(QThread):  # 线程2
    signal = pyqtSignal()

    def __init__(self, signal):
        super().__init__()
        # self.signal.connect(self.f)

    def f(self):
        for i in range(10):
            print(i)
            time.sleep(1)

    def run(self):
        while True:
            print('.', end='')
            time.sleep(1)


class MyWin(QWidget):
    main_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        # 按钮初始化
        self.btn_1 = QPushButton('按钮1', self)
        self.btn_1.setCheckable(True)
        self.btn_1.move(120, 80)
        self.btn_1.clicked.connect(self.click_1)  # 绑定槽函数

        self.btn_2 = QPushButton('按钮2', self)
        self.btn_2.setCheckable(True)
        self.btn_2.move(120, 120)
        self.btn_2.clicked.connect(self.click_2)  # 绑定槽函数

        self.thread = PreventFastClickThreadSignal()
        # self.thread.signal.connect(self.thread.f)
        self.thread.start()

    def click_1(self):
        print('click_1')

    def click_2(self):
        print('click_2')
        self.thread.signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWin()
    myshow.show()
    sys.exit(app.exec_())
