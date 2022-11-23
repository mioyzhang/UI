# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testWidgets.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 268)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/icon/icon/飞机.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_label = QtWidgets.QLabel(Form)
        self.label_label.setObjectName("label_label")
        self.verticalLayout.addWidget(self.label_label)
        self.label_label_content = QtWidgets.QLabel(Form)
        self.label_label_content.setObjectName("label_label_content")
        self.verticalLayout.addWidget(self.label_label_content)
        self.horizontalLayout_other = QtWidgets.QHBoxLayout()
        self.horizontalLayout_other.setObjectName("horizontalLayout_other")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_other.addItem(spacerItem)
        self.label_icon_img = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.label_icon_img.sizePolicy().hasHeightForWidth())
        self.label_icon_img.setSizePolicy(sizePolicy)
        self.label_icon_img.setText("")
        self.label_icon_img.setPixmap(QtGui.QPixmap(":/icon/icon/图像.png"))
        self.label_icon_img.setScaledContents(True)
        self.label_icon_img.setObjectName("label_icon_img")
        self.horizontalLayout_other.addWidget(self.label_icon_img)
        self.label_icon_file = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.label_icon_file.sizePolicy().hasHeightForWidth())
        self.label_icon_file.setSizePolicy(sizePolicy)
        self.label_icon_file.setText("")
        self.label_icon_file.setPixmap(QtGui.QPixmap(":/icon/icon/文件.png"))
        self.label_icon_file.setScaledContents(True)
        self.label_icon_file.setObjectName("label_icon_file")
        self.horizontalLayout_other.addWidget(self.label_icon_file)
        self.verticalLayout.addLayout(self.horizontalLayout_other)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_label.setText(_translate("Form", "NodeLabel"))
        self.label_label_content.setText(_translate("Form", "content"))


import resouce_rc
