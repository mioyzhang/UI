# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dell/workspace/UI/ui/test.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import MessageEditWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(889, 564)
        self.widget = MessageEditWidget(Form)
        self.widget.setGeometry(QtCore.QRect(240, 50, 331, 271))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Test(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = Test()
    w.show()

    app.exec()