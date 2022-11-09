import sys
from PyQt5.Qt import *;
from PyQt5.QtCore import *;
from PyQt5.QtWidgets import *;

import resouce_rc

 
# 自定义的item 继承自QListWidgetItem
class customQListWidgetItem(QListWidgetItem):
    def __init__(self, name, img):
        super().__init__()
        # 自定义item中的widget 用来显示自定义的内容
        # self.widget = QWidget()
        # # 用来显示name
        # self.nameLabel = QLabel()
        # self.nameLabel.setText(name)
        # # 用来显示avator(图像)
        # self.avatorLabel = QLabel()
        # # 设置图像源 和 图像大小
        # # self.avatorLabel.setPixmap(QPixmap(img).scaled(50, 50))
        # self.avatorLabel.setPixmap(QPixmap(":/icon/icon/cat.png").scaled(50, 50))
        # # 设置布局用来对nameLabel和avatorLabel进行布局
        # self.hbox = QHBoxLayout()
        # self.hbox.addWidget(self.avatorLabel)
        # self.hbox.addWidget(self.nameLabel)
        # self.hbox.addStretch(1)
        # # 设置widget的布局
        # self.widget.setLayout(self.hbox)
        # # 设置自定义的QListWidgetItem的sizeHint，不然无法显示
        # self.setSizeHint(self.widget.sizeHint())
        
        self.widget = QWidget()
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.widget)
        self.label.setMaximumSize(QSize(41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(":/icon/icon/cat.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.label_2.setText("n1")
        self.label_3.setText( "192.168.0.15")
        self.pushButton.setText("测试连接")
        self.pushButton_2.setText("发送消息")

        self.setSizeHint(self.widget.sizeHint())


 
if __name__ == "__main__":
    app = QApplication(sys.argv)
 
    # 主窗口
    w = QWidget()
    w.setWindowTitle("QListWindow")
    # 新建QListWidget
    listWidget = QListWidget(w)
 
    # 新建两个自定义的QListWidgetItem(customQListWidgetItem)
    item1 = customQListWidgetItem("鲤鱼王", "liyuwang.jpg")
    item2 = customQListWidgetItem("可达鸭", "kedaya.jpg")
 
    # 在listWidget中加入两个自定义的item
    listWidget.addItem(item1)
    listWidget.setItemWidget(item1, item1.widget)
    listWidget.addItem(item2)
    listWidget.setItemWidget(item2, item2.widget)
 
    # 绑定点击槽函数 点击显示对应item中的name
    listWidget.itemClicked.connect(lambda item: print(item.nameLabel.text()))
 
    w.show()
    sys.exit(app.exec_())
