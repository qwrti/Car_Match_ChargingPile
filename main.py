
###########################导入所需的库########################
import os
import sys
import time
import math
from PyQt5.QtCore import QUrl, pyqtSlot, QObject, pyqtSignal, QTimer
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np

#############导入UI界面的设置文件(Ui_main.py)#################
from class_MainWindow import TInteractObj,MainWindow
from Ui_main import Ui_MainWindow

## 使用QT自己的方法建立整个APP的界面，使用的就是“PyQt5.py”中定义的方法
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())