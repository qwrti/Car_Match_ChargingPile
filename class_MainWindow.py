## import libraries ##
import os
import sys
import time
import math
from PyQt5.QtCore import QUrl, pyqtSlot, QObject, pyqtSignal, QTimer
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np

from Ui_main import Ui_MainWindow
# from f1_receive_data import receive_data
def receive_data():
    pass
## 回调函数用于处理从JavaScript接收到的数据 ##
class TInteractObj(QObject):
    sig_send_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 交互对象接收到js调用后执行的回调函数.
        self.receive_str_from_js_callback = None

    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        self.receive_str_from_js_callback(str)

## 用于设置UI控制界面中按钮等其他控件的用途 ##
class MainWindow(QMainWindow, Ui_MainWindow):
    ##构造方法
    def __init__(self, parent=None):
        #调用父类的构造方法，将当前对象作为参数传递
        super(MainWindow, self).__init__(parent)
        #调用Ui_MainWindow类的setupUi方法，设置UI界面
####################这边定义的变量都意义不明，需要大改。感觉既然已经把receive_data给拆分出去了，那这些变量完全可以搬到类外来定义####################
####################尤其是如果都定义为私有变量，其他接口要使用也很麻烦，不如把类里面能在外部定义的变量就在外部定义了##################
        self.setupUi(self)
        self.count = 50
        self.last_p = []
        text = self.textEdit_2.toPlainText()
        print (text)
        self.gps_start = []
        self.car_c = np.ones([50], dtype=np.uint8) * (-1)
        self.post = '106.615559,29.538386,106.612811,29.535215,106.61803,29.536547,106.612397,29.546053,106.615704,29.537384,106.611434,29.535636,106.612279,29.538397,106.610106,29.533026,106.613436,29.540303,106.616361,29.535254,106.618242,29.532338,106.609128,29.540774,106.610177,29.535436'
        self.post_ = np.array(
            [106.615559, 29.538386, 106.612811, 29.535215, 106.61803, 29.536547, 106.612397, 29.546053, 106.615704,
             29.537384, 106.611434, 29.535636, 106.612279, 29.538397, 106.610106, 29.533026, 106.613436, 29.540303,
             106.616361, 29.535254, 106.618242, 29.532338, 106.609128, 29.540774, 106.610177, 29.535436])

        #随机生成普通地图上的起点终点信息
        self.post_num = np.ones([26], dtype=np.uint8)
        self.point = []
        self.power = np.random.rand(50) * 0.7 + 0.3  # 函数返回一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1。
        self.index = (os.path.split(os.path.realpath(__file__))[0]) + "/index.html"
        self.webview.load(QUrl.fromLocalFile(self.index))
        self.init_channel()
################# 一个qi,一个qi0,一个qidian，这些都是啥呀 ####################
        self.qi = np.array([106.614248, 29.53727]) + (np.random.rand(50, 2) - 0.5) / 100
        self.qi0 = list(map(str, self.qi.reshape(1, -1).tolist()))
        self.noword = 0

    ## 功能：初始化一个QWebChannel对象，并将其注册到webview的页面上 ##        
    def init_channel(self):
        self.interact_obj = TInteractObj(self)
        self.interact_obj.receive_str_from_js_callback =receive_data
        ## 创建一个QWebChannel对象，将webview的页面作为参数传递给它
        channel = QWebChannel(self.webview.page())
        # interact_obj 为交互对象的名字,会在js中使用
        #使用registerObject方法将interact_obj对象注册到channel中，并命名为"interact_obj"
        channel.registerObject("interact_obj", self.interact_obj)
        # 使用setWebChannel方法将创建的channel设置到webview的页面上
        self.webview.page().setWebChannel(channel)
        

            