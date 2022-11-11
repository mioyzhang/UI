import os
import sys
import time
import json
import random
import math

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QThread

from ui.edit import Ui_EditForm

from tools import generate_random_gps


class Message(object):
    def __init__(self, sequence=None, type=None, content=None, with_gps=False, gps=None, files=[], images=[]):
        super(Message, self).__init__()
        self.sequence = sequence
        self.type = type
        self.content = content
        self.with_gps = with_gps
        self.gps = gps
        self.files = files
        self.images = images
    
    def to_dict(self):
        message_dict = {
            'sequence': self.sequence,
            'type': self.type,
            'content': self.content,
            'with_gps': self.with_gps,
            'gps': self.gps,
            'files': self.files,
            'images': self.images
        }
        return message_dict

    def to_json(self):
        message_json = json.dumps(self.to_dict())
        return message_json
    
    def __str__(self) -> str:
        return self.to_json()


class Packet(object):
    def __init__(self) -> None:
        super().__init__()
        
        self.message = None
        self.src = None
        self.dst = None

        pass


class EditWidget(QWidget, Ui_EditForm):
    message = None

    def __init__(self):
        super(EditWidget, self).__init__()
        self.setupUi(self)

        self.listWidget_files.hide()
        self.listWidget_images.hide()

        self.setWindowIcon(QIcon('resource/icon/cat.png'))
        self.init_connect()

    def init_connect(self):
        self.pushButton_position.clicked.connect(self.generate_random_gps)
        self.pushButton_generate.clicked.connect(self.generate_random_gps)
        self.pushButton_submit.clicked.connect(self.extract)

        self.toolButton_file.clicked.connect(self.choose_file)
        self.toolButton_img.clicked.connect(self.choose_image)

        self.listWidget_files.itemDoubleClicked['QListWidgetItem*'].connect(lambda: self.listWidget_files.takeItem(self.listWidget_files.currentRow()))
        self.listWidget_images.itemDoubleClicked['QListWidgetItem*'].connect(lambda: self.listWidget_images.takeItem(self.listWidget_images.currentRow()))

    def generate_random_gps(self):
        longitude, latitude = generate_random_gps()
        self.lineEdit.setText(f'{longitude}, {latitude}')

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
        imagename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), image_filter)
        imagename = imagename[0]
        self.listWidget_images.show()
        for i in imagename:
            self.listWidget_images.addItem(i)
        print(imagename)

    def extract(self):

        sequence = self.label_seq.text()
        type = self.comboBox.currentText()
        content = self.textEdit.toPlainText()
        with_gps = self.radioButton.isChecked()
        gps = self.lineEdit.text()

        files = [self.listWidget_files.item(i).text() for i in range(self.listWidget_files.count())]
        images = [self.listWidget_images.item(i).text() for i in range(self.listWidget_images.count())]

        self.message = Message(sequence, type, content, with_gps, gps, files, images)
        print(self.message)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = EditWidget()
    w.show()

    app.exec()
