####################导入必要的库#######################
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap,QPalette,QFont
import sys

###################### 常量定义 ############
text_length_s = 80
text_width_s = 40
button_length_s = 80
button_width_s = 20

label_car_start_postion_len = 0
label_car_start_postion_wid = 100

label_length = 80
label_width = 40

label_pile_start_postion_len = 0
label_pile_start_postion_wid = 700
####################定义一个名为Ui_MainWindow的类################### 
'''
这段代码使用PyQt5库创建了一个简单的图形用户界面，包括一个文本编辑框、
一个按钮和一个网页浏览器。用户可以在文本编辑框中输入文本，点击按钮后，
文本将被显示在网页浏览器中。'''
#在这个类中，定义了两个方法：setupUi和retranslateUi。
class Ui_MainWindow(object):
    
    #setupUi方法：这个方法用于设置UI界面
    def setupUi(self, MainWindow):

        #设置窗口对象名称为“MainWindow”
        MainWindow.setObjectName("MainWindow")
        #调整窗口大小为800*620
        MainWindow.resize(1000, 800)
        
        #创建一个网格布局(QGridLayout)
        layout = QGridLayout()
        
        #创建一个名为centralwidget的QWidget对象
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #并将其设置为窗口的中心部件
        self.centralwidget.setObjectName("centralwidget")
        
        #创建一个名为gridLayout的QGridLayout对象，并将其设置为centralwidget的布局
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        # self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setReadOnly(False)
        # self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        #################这一段有点迷惑##############
        #创建一个名为textEdit_2的QTextEdit对象，并将其添加到gridLayout中
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, text_length_s,text_width_s))
        self.textEdit.setObjectName("textEdit")
        
        #获取textEdit_2中的纯文本内容并将其赋值给变量text
        text = self.textEdit.toPlainText()


########################### 添加按钮 #############################
        ########“将其添加到gridLayout中”这一句有点迷惑#########
        #创建一个名为pushButton的QPushButton对象
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(0, text_width_s, button_length_s,button_width_s))
        self.pushButton.setObjectName("pushButton")
        
        self.nameLineEdit = QLineEdit(" ")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        #将其添加到gridLayout中
        self.gridLayout.addWidget(self.pushButton2, 1, 0, 1, 1)
        
        self.pushButton3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton3.setGeometry(QtCore.QRect(text_length_s, text_width_s, button_length_s,button_width_s))
        self.pushButton3.setObjectName("pushButton3")   
                
        #创建一个名为webview的QWebEngineView对象
        self.webview = QWebEngineView(self.centralwidget)
        self.webview.setObjectName("webview")
        self.webview.setMinimumWidth(400)
        #将webview添加到gridLayout中
        self.gridLayout.addWidget(self.webview, 0, 1, 2, 1)
        #将centralwidget设置为窗口的中心部件
        MainWindow.setCentralWidget(self.centralwidget)
        #调用retranslateUi方法进行界面翻译
        self.retranslateUi(MainWindow)
        #通过QMetaObject.connectSlotsByName方法连接信号和槽
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#################### 添加标签Label ###################
        # 创建一个名为label_current_position的QLabel对象
        self.label_current_position = QtWidgets.QLabel(self.centralwidget)
        self.label_current_position.setGeometry(QtCore.QRect(label_car_start_postion_len\
            , label_car_start_postion_wid,label_car_start_postion_len + label_length,\
                label_car_start_postion_wid + label_width))
        self.label_current_position.setObjectName("label_current_position")
        # 设置标签的文本为“当前位置”
        self.label_current_position.setText("当前位置:")
        # 将label_current_position添加到gridLayout中
        # self.gridLayout.addWidget(self.label_current_position, 0, 0, 1, 1)

        # 创建一个名为label_order_num的QLabel对象
        self.label_current_position = QtWidgets.QLabel(self.centralwidget)
        self.label_current_position.setGeometry(QtCore.QRect(label_car_start_postion_len\
            , label_car_start_postion_wid + label_width, label_car_start_postion_len + label_length,\
                label_length +label_car_start_postion_wid + label_width*2))
        self.label_current_position.setObjectName("label_order_num")
        self.label_current_position.setText("订单编号:")

        # 创建一个名为label_surplus_ele的QLabel对象
        self.label_current_position = QtWidgets.QLabel(self.centralwidget)
        self.label_current_position.setGeometry(QtCore.QRect(label_car_start_postion_len\
            , label_car_start_postion_wid + label_width*2, label_car_start_postion_len + label_length,\
                label_length +label_car_start_postion_wid + label_width*3))
        self.label_current_position.setObjectName("label_surplus_ele")
        self.label_current_position.setText("剩余电量:")
        
        
        self.label_current_position = QtWidgets.QLabel(self.centralwidget)
        self.label_current_position.setGeometry(QtCore.QRect(label_pile_start_postion_len,\
            label_car_start_postion_wid, label_car_start_postion_len + label_length, \
                label_pile_start_postion_wid + label_width))
        self.label_current_position.setObjectName("choice1")
        # 设置标签的文本为“当前位置”
        self.label_current_position.setText("推荐1:")
        
        self.label_current_position = QtWidgets.QLabel(self.centralwidget)
        self.label_current_position.setGeometry(QtCore.QRect(label_pile_start_postion_len,\
        label_car_start_postion_wid + label_width, label_car_start_postion_len + label_length, \
        label_pile_start_postion_wid + label_width*2))
        self.label_current_position.setObjectName("choice2")
        # 设置标签的文本为“当前位置”
        self.label_current_position.setText("推荐2:")
        
        self.label_current_position = QtWidgets.QLabel(self.centralwidget)
        self.label_current_position.setGeometry(QtCore.QRect(label_pile_start_postion_len,\
        label_car_start_postion_wid + label_width*2, label_car_start_postion_len + label_length, \
        label_pile_start_postion_wid + label_width*3))
        self.label_current_position.setObjectName("choice3")
        # 设置标签的文本为“当前位置”
        self.label_current_position.setText("推荐3:")
        
####################################################################################
        # 创建一个名为resultTextEdit的QTextEdit对象，并将其添加到gridLayout中
        self.resultTextEdit = QtWidgets.QTextEdit(MainWindow)
        self.resultTextEdit.setObjectName("resultTextEdit")
        self.gridLayout.addWidget(self.resultTextEdit, 3, 0, 1, 2)
##################根据当前的语言环境翻译界面上的文本################
    def retranslateUi(self, MainWindow):
        #创建一个名为_translate的函数，接受一个字符串参数并返回其翻译后的字符串
        _translate = QtCore.QCoreApplication.translate
        #将窗口的标题设置为"MainWindow"
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        #设置第一个按钮，名为“传入输入数据”
        self.pushButton.setText(_translate("MainWindow", "输入"))
        
        #设置第二个按钮，名为“联网并开始导航”
        self.pushButton2.setText(_translate("MainWindow", "启动订单"))
        
        #设置第三个按钮，名为“定位”
        self.pushButton3.setText(_translate("MainWindow", "定位"))