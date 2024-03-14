import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()  # 对QWidget继承
        '''设置主界面参数'''
        self.setWindowTitle("MainWindow")  # 设置主界面标题
        self.setGeometry(450, 450, 500, 500)

        '''功能页面的文本文字'''
        # 头顶界面文字
        self.label = QLabel(self)
        # 设置字体->文字
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(15)
        font.setBold(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setText(u'电动车导航系统')
        self.label.setGeometry(0, 0, 500, 50)

        '''文本显示显示 使用到布局管理器'''
        ww = QWidget(self)
        vbox = QVBoxLayout(ww)
        ww.move(340, 50)
        ww.resize(165, 200)

        hbox = QHBoxLayout()
        label_strat = QLabel('起始点')
        self.line_edit_start = QLineEdit()
        hbox.addWidget(label_strat)
        hbox.addWidget(self.line_edit_start)
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label_end = QLabel('目的地')
        self.line_edit_end = QLineEdit()
        hbox.addWidget(label_end)
        hbox.addWidget(self.line_edit_end)
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label_chargepile = QLabel('最近充电桩')
        self.line_label_charge_pos = QLabel()  # 充电桩位置显示
        hbox.addWidget(label_chargepile)
        hbox.addWidget(self.line_label_charge_pos)
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label_chargeval = QLabel('电价')
        self.line_label_charge_val = QLabel()  # 充电桩价格显示
        hbox.addWidget(label_chargeval)
        hbox.addWidget(self.line_label_charge_val)
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        '''添加按钮'''
        hbox = QHBoxLayout()
        self.button_search = QPushButton('开始搜索', self)  # 搜索按钮
        self.button_search.move(20, 20)
        self.button_search.clicked.connect(self.on_button_search_clicked)
        self.button_search.resize(160, 40)
        hbox.addWidget(self.button_search)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label_car_pos = QLabel('车辆地址')
        self.line_label_car_pos = QLabel()
        hbox.addWidget(label_car_pos)
        hbox.addWidget(self.line_label_car_pos)
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label_car_id = QLabel('车辆ID')
        self.line_label_car_id = QLabel()
        hbox.addWidget(label_car_id)
        hbox.addWidget(self.line_label_car_id)
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        ww.setLayout(vbox)

        '''地图页面显示'''
        map = QWebEngineView(self)
        map.setGeometry(0, 50, 340, 350)
        map_url = QUrl(QFileInfo("./index.html").absoluteFilePath())
        map.setUrl(map_url)

    '''button_search按键功能函数'''
    # 函数实现对起点、终点输入框的文字输入读取
    def on_button_search_clicked(self):
        text_start = self.line_edit_start.text().strip()  # 获取输入框中的文本数据，清除末尾的空格
        text_end = self.line_edit_end.text().strip()  # 获取输入框中的文本数据，清除末尾的空格
        print('起始点:', text_start, ';', '终点:', text_end, ';')

        '''加入算法进行充电桩选择 目前先用随机数代替'''
        self.line_label_charge_pos.setText(str(random.randint(0, 100)) + ' , ' + str(random.randint(0, 100)))  # 充电桩
        self.line_label_charge_val.setText(str(random.randint(0, 100)) + '元/度')  # 充电站电费
        self.line_label_car_pos.setText(str(random.randint(0, 100)) + ' , ' + str(random.randint(0, 100)))  # 车辆地址
        self.line_label_car_id.setText(str(random.randint(0, 100)))  # 车辆编号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.show()
    sys.exit(app.exec_())
