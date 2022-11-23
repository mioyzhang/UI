# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(81, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("QWidget#page_3{image:url(:/img/img/战场态势.jpg)}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_26 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_5.addWidget(self.label_26)
        self.listWidget_messages = QtWidgets.QListWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_messages.sizePolicy().hasHeightForWidth())
        self.listWidget_messages.setSizePolicy(sizePolicy)
        self.listWidget_messages.setObjectName("listWidget_messages")
        self.verticalLayout_5.addWidget(self.listWidget_messages)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.stackedWidget_message = QtWidgets.QStackedWidget(self.page)
        self.stackedWidget_message.setObjectName("stackedWidget_message")
        self.page_message_view = QtWidgets.QWidget()
        self.page_message_view.setObjectName("page_message_view")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_message_view)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.viewWidget = MessageViewWidget(self.page_message_view)
        self.viewWidget.setObjectName("viewWidget")
        self.horizontalLayout_4.addWidget(self.viewWidget)
        self.widget_7 = QtWidgets.QWidget(self.page_message_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_7)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_time = QtWidgets.QLabel(self.widget_2)
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_time, 4, 1, 1, 1)
        self.label_dst = QtWidgets.QLabel(self.widget_2)
        self.label_dst.setText("")
        self.label_dst.setObjectName("label_dst")
        self.gridLayout.addWidget(self.label_dst, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_protocol = QtWidgets.QLabel(self.widget_2)
        self.label_protocol.setText("")
        self.label_protocol.setObjectName("label_protocol")
        self.gridLayout.addWidget(self.label_protocol, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_gps = QtWidgets.QLabel(self.widget_2)
        self.label_gps.setText("")
        self.label_gps.setObjectName("label_gps")
        self.gridLayout.addWidget(self.label_gps, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_src = QtWidgets.QLabel(self.widget_2)
        self.label_src.setText("")
        self.label_src.setObjectName("label_src")
        self.gridLayout.addWidget(self.label_src, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_TR = QtWidgets.QLabel(self.widget_2)
        self.label_TR.setText("")
        self.label_TR.setObjectName("label_TR")
        self.gridLayout.addWidget(self.label_TR, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_4.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem)
        self.widget_4 = QtWidgets.QWidget(self.widget_7)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.widget_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_last_seen = QtWidgets.QLabel(self.widget_3)
        self.label_last_seen.setText("")
        self.label_last_seen.setObjectName("label_last_seen")
        self.gridLayout_2.addWidget(self.label_last_seen, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_label = QtWidgets.QLabel(self.widget_3)
        self.label_label.setText("")
        self.label_label.setObjectName("label_label")
        self.gridLayout_2.addWidget(self.label_label, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_address = QtWidgets.QLabel(self.widget_3)
        self.label_address.setText("")
        self.label_address.setObjectName("label_address")
        self.gridLayout_2.addWidget(self.label_address, 1, 1, 1, 1)
        self.label_node_type = QtWidgets.QLabel(self.widget_3)
        self.label_node_type.setText("")
        self.label_node_type.setObjectName("label_node_type")
        self.gridLayout_2.addWidget(self.label_node_type, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.widget_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 420, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.widget_7)
        self.stackedWidget_message.addWidget(self.page_message_view)
        self.page_message_edit = QtWidgets.QWidget()
        self.page_message_edit.setObjectName("page_message_edit")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_message_edit)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox = QtWidgets.QGroupBox(self.page_message_edit)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.editWidget = MessageEditWidget(self.groupBox)
        self.editWidget.setObjectName("editWidget")
        self.verticalLayout_11.addWidget(self.editWidget)
        self.verticalLayout_14.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.page_message_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 240))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.comboBox_dst = QtWidgets.QComboBox(self.tab)
        self.comboBox_dst.setObjectName("comboBox_dst")
        self.horizontalLayout_8.addWidget(self.comboBox_dst)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.radioButton_address = QtWidgets.QRadioButton(self.tab)
        self.radioButton_address.setObjectName("radioButton_address")
        self.horizontalLayout_9.addWidget(self.radioButton_address)
        self.lineEdit_address = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_address.setEnabled(False)
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.horizontalLayout_9.addWidget(self.lineEdit_address)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.comboBox_protocol = QtWidgets.QComboBox(self.tab)
        self.comboBox_protocol.setObjectName("comboBox_protocol")
        self.comboBox_protocol.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_protocol)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        spacerItem3 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem4)
        self.pushButton_send = QtWidgets.QPushButton(self.tab)
        self.pushButton_send.setObjectName("pushButton_send")
        self.verticalLayout_13.addWidget(self.pushButton_send)
        self.pushButton_p1_test = QtWidgets.QPushButton(self.tab)
        self.pushButton_p1_test.setObjectName("pushButton_p1_test")
        self.verticalLayout_13.addWidget(self.pushButton_p1_test)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        spacerItem5 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_14.addWidget(self.tabWidget)
        self.stackedWidget_message.addWidget(self.page_message_edit)
        self.horizontalLayout_5.addWidget(self.stackedWidget_message)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget_nodes = QtWidgets.QListWidget(self.page_2)
        self.listWidget_nodes.setObjectName("listWidget_nodes")
        self.verticalLayout.addWidget(self.listWidget_nodes)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.pushButton_p2_test = QtWidgets.QPushButton(self.page_2)
        self.pushButton_p2_test.setObjectName("pushButton_p2_test")
        self.horizontalLayout_3.addWidget(self.pushButton_p2_test)
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.widget_5)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_9.addWidget(self.label_27)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_d_label = QtWidgets.QLabel(self.widget_6)
        self.label_d_label.setText("")
        self.label_d_label.setObjectName("label_d_label")
        self.gridLayout_3.addWidget(self.label_d_label, 0, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.widget_6)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 1, 0, 1, 1)
        self.label_d_ip = QtWidgets.QLabel(self.widget_6)
        self.label_d_ip.setText("")
        self.label_d_ip.setObjectName("label_d_ip")
        self.gridLayout_3.addWidget(self.label_d_ip, 1, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.widget_6)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 3, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget_6)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 2, 0, 1, 1)
        self.label_d_type = QtWidgets.QLabel(self.widget_6)
        self.label_d_type.setText("")
        self.label_d_type.setObjectName("label_d_type")
        self.gridLayout_3.addWidget(self.label_d_type, 2, 1, 1, 1)
        self.label_d_time = QtWidgets.QLabel(self.widget_6)
        self.label_d_time.setText("")
        self.label_d_time.setObjectName("label_d_time")
        self.gridLayout_3.addWidget(self.label_d_time, 3, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.widget_6)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_6)
        self.verticalLayout_10.addWidget(self.widget_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menuEdit.addAction(self.action_2)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_message.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.radioButton_address.clicked['bool'].connect(self.lineEdit_address.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "控制中心"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "消息队列"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "节点列表"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "战场态势"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_26.setText(_translate("MainWindow", "消息队列"))
        self.label_7.setText(_translate("MainWindow", "消息详情"))
        self.label_10.setText(_translate("MainWindow", "时间："))
        self.label_3.setText(_translate("MainWindow", "源节点："))
        self.label_5.setText(_translate("MainWindow", "目的节点："))
        self.label_9.setText(_translate("MainWindow", "协议："))
        self.label_13.setText(_translate("MainWindow", "GPS："))
        self.label_2.setText(_translate("MainWindow", "消息类型："))
        self.label_8.setText(_translate("MainWindow", "节点详情"))
        self.label_21.setText(_translate("MainWindow", "last seen："))
        self.label_19.setText(_translate("MainWindow", "节点类型"))
        self.label_17.setText(_translate("MainWindow", "节点地址："))
        self.label_15.setText(_translate("MainWindow", "节点标签："))
        self.groupBox.setTitle(_translate("MainWindow", "编辑消息"))
        self.label_14.setText(_translate("MainWindow", "目的节点："))
        self.radioButton_address.setText(_translate("MainWindow", "其它地址："))
        self.label_16.setText(_translate("MainWindow", "传输协议："))
        self.comboBox_protocol.setItemText(0, _translate("MainWindow", "TCP"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))
        self.pushButton_p1_test.setText(_translate("MainWindow", "test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "单播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "广播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "组播"))
        self.label.setText(_translate("MainWindow", "节点列表"))
        self.pushButton_p2_test.setText(_translate("MainWindow", "test"))
        self.pushButton.setText(_translate("MainWindow", "扫描节点"))
        self.label_27.setText(_translate("MainWindow", "节点详情"))
        self.label_30.setText(_translate("MainWindow", "节点地址："))
        self.label_34.setText(_translate("MainWindow", "last see："))
        self.label_32.setText(_translate("MainWindow", "节点类型"))
        self.label_28.setText(_translate("MainWindow", "节点标签："))
        self.menu.setTitle(_translate("MainWindow", "窗口"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.action.setText(_translate("MainWindow", "消息队列"))
        self.action_3.setText(_translate("MainWindow", "节点列表"))
        self.action_5.setText(_translate("MainWindow", "战场态势"))
        self.action_6.setText(_translate("MainWindow", "控制中心设置"))
        self.action_2.setText(_translate("MainWindow", "新建消息"))
from widgets import MessageEditWidget, MessageViewWidget
import resouce_rc
