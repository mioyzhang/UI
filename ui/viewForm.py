# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewForm(object):
    def setupUi(self, ViewForm):
        ViewForm.setObjectName("ViewForm")
        ViewForm.resize(778, 584)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ViewForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(ViewForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_seq = QtWidgets.QLabel(ViewForm)
        self.label_seq.setObjectName("label_seq")
        self.horizontalLayout.addWidget(self.label_seq)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(ViewForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_type = QtWidgets.QLabel(ViewForm)
        self.label_type.setObjectName("label_type")
        self.horizontalLayout_2.addWidget(self.label_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(ViewForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_gps = QtWidgets.QLabel(ViewForm)
        self.label_gps.setObjectName("label_gps")
        self.horizontalLayout_3.addWidget(self.label_gps)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(ViewForm)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textBrowser = QtWidgets.QTextBrowser(ViewForm)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(ViewForm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 758, 232))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_test1 = QtWidgets.QPushButton(ViewForm)
        self.pushButton_test1.setObjectName("pushButton_test1")
        self.horizontalLayout_5.addWidget(self.pushButton_test1)
        self.pushButton_test2 = QtWidgets.QPushButton(ViewForm)
        self.pushButton_test2.setObjectName("pushButton_test2")
        self.horizontalLayout_5.addWidget(self.pushButton_test2)
        self.pushButton_cancel = QtWidgets.QPushButton(ViewForm)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_5.addWidget(self.pushButton_cancel)
        self.pushButton_submit = QtWidgets.QPushButton(ViewForm)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.horizontalLayout_5.addWidget(self.pushButton_submit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(ViewForm)
        QtCore.QMetaObject.connectSlotsByName(ViewForm)

    def retranslateUi(self, ViewForm):
        _translate = QtCore.QCoreApplication.translate
        ViewForm.setWindowTitle(_translate("ViewForm", "Form"))
        self.label_2.setText(_translate("ViewForm", "序列号： "))
        self.label_seq.setText(_translate("ViewForm", "TextLabel"))
        self.label.setText(_translate("ViewForm", "消息类型:"))
        self.label_type.setText(_translate("ViewForm", "TextLabel"))
        self.label_7.setText(_translate("ViewForm", "GPS:     "))
        self.label_gps.setText(_translate("ViewForm", "TextLabel"))
        self.label_4.setText(_translate("ViewForm", "描述："))
        self.pushButton_test1.setText(_translate("ViewForm", "test1"))
        self.pushButton_test2.setText(_translate("ViewForm", "test2"))
        self.pushButton_cancel.setText(_translate("ViewForm", "取消"))
        self.pushButton_submit.setText(_translate("ViewForm", "确定"))
import resouce_rc