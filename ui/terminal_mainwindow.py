# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terminal_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TerminalMainWindow(object):
    def setupUi(self, TerminalMainWindow):
        TerminalMainWindow.setObjectName("TerminalMainWindow")
        TerminalMainWindow.resize(1420, 798)
        self.centralwidget = QtWidgets.QWidget(TerminalMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 80, 258, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(360, 80, 521, 311))
        self.widget_4.setObjectName("widget_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(370, 430, 531, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(50, 30, 54, 12))
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 67, 22))
        self.comboBox.setObjectName("comboBox")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(40, 70, 83, 16))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(60, 110, 54, 12))
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 110, 67, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1020, 60, 291, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        TerminalMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TerminalMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 22))
        self.menubar.setObjectName("menubar")
        TerminalMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TerminalMainWindow)
        self.statusbar.setObjectName("statusbar")
        TerminalMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TerminalMainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.radioButton.clicked['bool'].connect(self.lineEdit.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TerminalMainWindow)

    def retranslateUi(self, TerminalMainWindow):
        _translate = QtCore.QCoreApplication.translate
        TerminalMainWindow.setWindowTitle(_translate("TerminalMainWindow", "射手/传感器"))
        self.label.setText(_translate("TerminalMainWindow", "消息队列"))
        self.label_14.setText(_translate("TerminalMainWindow", "目的地址："))
        self.radioButton.setText(_translate("TerminalMainWindow", "其它地址："))
        self.label_15.setText(_translate("TerminalMainWindow", "传输协议："))
        self.comboBox_2.setItemText(0, _translate("TerminalMainWindow", "TCP"))
        self.comboBox_2.setItemText(1, _translate("TerminalMainWindow", "UDP"))
        self.pushButton.setText(_translate("TerminalMainWindow", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TerminalMainWindow", "单播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TerminalMainWindow", "广播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("TerminalMainWindow", "组播"))
        self.groupBox.setTitle(_translate("TerminalMainWindow", "控制中心"))
        self.label_2.setText(_translate("TerminalMainWindow", "IP地址："))
        self.label_4.setText(_translate("TerminalMainWindow", "TextLabel"))
        self.label_3.setText(_translate("TerminalMainWindow", "端口号："))
        self.label_5.setText(_translate("TerminalMainWindow", "TextLabel"))
        self.label_6.setText(_translate("TerminalMainWindow", "状态："))
        self.label_7.setText(_translate("TerminalMainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("TerminalMainWindow", "传感器射手"))
        self.label_8.setText(_translate("TerminalMainWindow", "IP地址："))
        self.label_9.setText(_translate("TerminalMainWindow", "TextLabel"))
        self.label_10.setText(_translate("TerminalMainWindow", "端口号："))
        self.label_11.setText(_translate("TerminalMainWindow", "TextLabel"))
        self.label_12.setText(_translate("TerminalMainWindow", "状态："))
        self.label_13.setText(_translate("TerminalMainWindow", "TextLabel"))
