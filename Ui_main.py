####################导入必要的库#######################
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap,QPalette
import sys

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
        MainWindow.resize(800, 620)
        
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
        self.textEdit_2 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 81, 201))
        self.textEdit_2.setObjectName("textEdit_2")
        
        #获取textEdit_2中的纯文本内容并将其赋值给变量text
        text = self.textEdit_2.toPlainText()
        
        ########“将其添加到gridLayout中”这一句有点迷惑#########
        #创建一个名为pushButton2的QPushButton对象
        self.pushButton2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton2.setGeometry(QtCore.QRect(36, 202, 51, 20))
        self.pushButton2.setObjectName("pushButton2")
        
        self.nameLineEdit = QLineEdit(" ")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        #将其添加到gridLayout中
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        
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

##################根据当前的语言环境翻译界面上的文本################
    def retranslateUi(self, MainWindow):
        #创建一个名为_translate的函数，接受一个字符串参数并返回其翻译后的字符串
        _translate = QtCore.QCoreApplication.translate
        #将窗口的标题设置为"MainWindow"
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #设置第一个按钮，名为“同步到web”
        self.pushButton.setText(_translate("MainWindow", "联网并开始导航"))
        #设置第二个按钮，名为“确定”
        self.pushButton2.setText(_translate("MainWindow", "传入输入数据"))
        
        self.pushButton3.setText(_translate("MainWindow", "查看最近充电桩信息"))