# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edgeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EdgeMainWindow(object):
    def setupUi(self, EdgeMainWindow):
        EdgeMainWindow.setObjectName("EdgeMainWindow")
        EdgeMainWindow.resize(1143, 869)
        self.centralwidget = QtWidgets.QWidget(EdgeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_msg_list = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_msg_list.sizePolicy().hasHeightForWidth())
        self.groupBox_msg_list.setSizePolicy(sizePolicy)
        self.groupBox_msg_list.setObjectName("groupBox_msg_list")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_msg_list)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_msgs = QtWidgets.QListWidget(self.groupBox_msg_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_msgs.sizePolicy().hasHeightForWidth())
        self.listWidget_msgs.setSizePolicy(sizePolicy)
        self.listWidget_msgs.setObjectName("listWidget_msgs")
        self.verticalLayout.addWidget(self.listWidget_msgs)
        self.horizontalLayout_5.addWidget(self.groupBox_msg_list)
        self.verticalLayout_middle = QtWidgets.QVBoxLayout()
        self.verticalLayout_middle.setObjectName("verticalLayout_middle")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.editWidget = MessageEditWidget(self.groupBox)
        self.editWidget.setObjectName("editWidget")
        self.verticalLayout_3.addWidget(self.editWidget)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 240))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.comboBox_dst = QtWidgets.QComboBox(self.tab)
        self.comboBox_dst.setObjectName("comboBox_dst")
        self.horizontalLayout.addWidget(self.comboBox_dst)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_address = QtWidgets.QRadioButton(self.tab)
        self.radioButton_address.setObjectName("radioButton_address")
        self.horizontalLayout_2.addWidget(self.radioButton_address)
        self.lineEdit_address = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_address.setEnabled(False)
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.horizontalLayout_2.addWidget(self.lineEdit_address)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.comboBox_protocol = QtWidgets.QComboBox(self.tab)
        self.comboBox_protocol.setObjectName("comboBox_protocol")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_protocol)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButton_send = QtWidgets.QPushButton(self.tab)
        self.pushButton_send.setObjectName("pushButton_send")
        self.verticalLayout_5.addWidget(self.pushButton_send)
        self.pushButton_test2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_test2.setObjectName("pushButton_test2")
        self.verticalLayout_5.addWidget(self.pushButton_test2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.viewWidget = MessageViewWidget(self.groupBox_4)
        self.viewWidget.setObjectName("viewWidget")
        self.verticalLayout_8.addWidget(self.viewWidget)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_middle.addWidget(self.stackedWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_middle)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_status = QtWidgets.QLabel(self.groupBox_2)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_delay = QtWidgets.QLabel(self.groupBox_2)
        self.label_delay.setObjectName("label_delay")
        self.gridLayout.addWidget(self.label_delay, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_c_address = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_c_address.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_c_address.sizePolicy().hasHeightForWidth())
        self.lineEdit_c_address.setSizePolicy(sizePolicy)
        self.lineEdit_c_address.setObjectName("lineEdit_c_address")
        self.gridLayout.addWidget(self.lineEdit_c_address, 0, 1, 1, 1)
        self.lineEdit_c_port = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_c_port.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_c_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_c_port.setSizePolicy(sizePolicy)
        self.lineEdit_c_port.setObjectName("lineEdit_c_port")
        self.gridLayout.addWidget(self.lineEdit_c_port, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_check = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_check.sizePolicy().hasHeightForWidth())
        self.pushButton_check.setSizePolicy(sizePolicy)
        self.pushButton_check.setObjectName("pushButton_check")
        self.horizontalLayout_6.addWidget(self.pushButton_check)
        self.pushButton_set = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_set.sizePolicy().hasHeightForWidth())
        self.pushButton_set.setSizePolicy(sizePolicy)
        self.pushButton_set.setCheckable(True)
        self.pushButton_set.setObjectName("pushButton_set")
        self.horizontalLayout_6.addWidget(self.pushButton_set)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_5.addWidget(self.widget)
        EdgeMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EdgeMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 22))
        self.menubar.setObjectName("menubar")
        EdgeMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EdgeMainWindow)
        self.statusbar.setObjectName("statusbar")
        EdgeMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EdgeMainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.radioButton_address.clicked['bool'].connect(self.lineEdit_address.setEnabled) # type: ignore
        self.pushButton_set.clicked['bool'].connect(self.lineEdit_c_address.setEnabled) # type: ignore
        self.pushButton_set.clicked['bool'].connect(self.lineEdit_c_port.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EdgeMainWindow)

    def retranslateUi(self, EdgeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        EdgeMainWindow.setWindowTitle(_translate("EdgeMainWindow", "射手/传感器"))
        self.groupBox_msg_list.setTitle(_translate("EdgeMainWindow", "消息队列"))
        self.groupBox.setTitle(_translate("EdgeMainWindow", "编辑消息"))
        self.label_14.setText(_translate("EdgeMainWindow", "目的节点："))
        self.radioButton_address.setText(_translate("EdgeMainWindow", "其它地址："))
        self.label_15.setText(_translate("EdgeMainWindow", "传输协议："))
        self.comboBox_protocol.setItemText(0, _translate("EdgeMainWindow", "TCP"))
        self.comboBox_protocol.setItemText(1, _translate("EdgeMainWindow", "UDP"))
        self.pushButton_send.setText(_translate("EdgeMainWindow", "发送"))
        self.pushButton_test2.setText(_translate("EdgeMainWindow", "test2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("EdgeMainWindow", "单播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("EdgeMainWindow", "广播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("EdgeMainWindow", "组播"))
        self.groupBox_4.setTitle(_translate("EdgeMainWindow", "消息"))
        self.groupBox_2.setTitle(_translate("EdgeMainWindow", "控制中心"))
        self.label_status.setText(_translate("EdgeMainWindow", "None"))
        self.label_6.setText(_translate("EdgeMainWindow", "状态："))
        self.label_delay.setText(_translate("EdgeMainWindow", "None"))
        self.label_21.setText(_translate("EdgeMainWindow", "时延"))
        self.label_2.setText(_translate("EdgeMainWindow", "IP地址："))
        self.label_3.setText(_translate("EdgeMainWindow", "端口号："))
        self.lineEdit_c_address.setText(_translate("EdgeMainWindow", "127.0.0.1"))
        self.lineEdit_c_port.setText(_translate("EdgeMainWindow", "8900"))
        self.pushButton_check.setText(_translate("EdgeMainWindow", "测试连接"))
        self.pushButton_set.setText(_translate("EdgeMainWindow", "设置"))
        self.groupBox_3.setTitle(_translate("EdgeMainWindow", "传感器/射手"))
        self.label_8.setText(_translate("EdgeMainWindow", "IP地址："))
        self.label_9.setText(_translate("EdgeMainWindow", "TextLabel"))
        self.label_10.setText(_translate("EdgeMainWindow", "端口号："))
        self.label_11.setText(_translate("EdgeMainWindow", "TextLabel"))
        self.label_12.setText(_translate("EdgeMainWindow", "状态："))
        self.label_13.setText(_translate("EdgeMainWindow", "TextLabel"))
from widgets import MessageEditWidget, MessageViewWidget
