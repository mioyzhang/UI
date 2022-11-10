import os
import sys
import time
import random
import math

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QThread

from ui.edit import Ui_EditForm


def generate_random_gps(base_log=None, base_lat=None, radius=None):
    """
    以（base_log, base_lat）为中心，radius为半径，生成随机GPS信息
    :param base_log:
    :param base_lat:
    :param radius:
    :return:
    """
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 这里是想保留6位小数点
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    return loga, lata


class MyWindow(QMainWindow, Ui_EditForm):
    sequence = None
    type = None
    content = None
    with_gps = False
    gps = None
    files = []
    images = []

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('resource/icon/cat.png'))
        self.init_connect()

    def init_connect(self):
        self.pushButton_position.clicked.connect(self.generate_random_gps)
        self.pushButton_generate.clicked.connect(self.generate_random_gps)
        self.pushButton_submit.clicked.connect(self.extract)

        self.toolButton_file.clicked.connect(self.choose_file)
        self.toolButton_img.clicked.connect(self.choose_image)

    def generate_random_gps(self):
        # 120.7 30为中国的中心位置
        longitude, latitude = generate_random_gps(base_log=120.7, base_lat=30, radius=1000000)
        self.lineEdit.setText(f'{longitude},{latitude}')

    def choose_file(self):
        file_filter = "All Files(*);;Text Files(*.txt)"
        filename = QFileDialog.getOpenFileNames(self, '选择文件', os.getcwd(), file_filter)
        print(filename)

    def choose_image(self):
        image_filter = "Image files (*.jpg *.png);;All Files(*)"
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), image_filter)
        print(filename)

    def extract(self):

        self.sequence = self.label_seq.text()
        self.type = self.comboBox.currentText()
        self.content = self.textEdit.toPlainText()
        self.with_gps = self.radioButton.isChecked()
        self.gps = self.lineEdit.text()

        print(self.sequence)
        print(self.type)
        print(self.content)
        print(self.with_gps)
        print(self.gps)
        print(self.files)
        print(self.images)

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
