import os
import sys
from PyQt5.QtWidgets import (QWidget,  QLabel,QVBoxLayout,QCheckBox,QGridLayout, QScrollArea,QApplication)
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt,QSize


class Picture(QWidget):
    def __init__(self, parent=None, url=None):
        super().__init__(parent)
        self.url = url
        self.ui()

    def ui(self):
        layout = QGridLayout()
        total = len(self.url)
        self.setLayout(layout)

        self.sc = QScrollArea(self)
        self.qw = QWidget()

        if total % 5 == 0:
            rows = int(total/5)
        else:
            rows = int(total/5) + 1
        self.qw.setMinimumSize(850,230*rows)
        for i in range(total):

            photo = QPixmap(imgs[i])

            width = photo.width()
            height = photo.height()
            if width==0 or height==0:
                continue
            tmp_image = photo.toImage()
            size = QSize(width,height)
            photo.convertFromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))
            tmp = QWidget(self.qw)
            vl = QVBoxLayout()
            label = QLabel()
            label.setFixedSize(150,200)
            label.setStyleSheet("border:1px solid gray")
            label.setPixmap(photo)
            label.setScaledContents(True)
            ck = QCheckBox(str(i)+"."+'sup'+"("+str(width)+"x"+str(height)+")", self)
            vl.addWidget(label)
            vl.addWidget(ck)
            tmp.setLayout(vl)
            tmp.move(160 * (i % 5), 230 * int(i / 5))

        self.sc.setWidget(self.qw)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    img_path = 'D:/Develop/PycharmProjects/UI/resource/icon'
    imgs = os.listdir(img_path)
    imgs = [os.path.join(img_path, i) for i in imgs]
    pic = Picture(url=imgs)

    pic.show()
    sys.exit(app.exec_())