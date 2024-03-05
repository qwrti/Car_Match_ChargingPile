from PyQt5.QtCore import pyqtSlot
from class_MainWindow import MainWindow
## 定义网页界面中每个按钮所对应的功能
def run():  ## ref 变 class
    global current_position='1,'  #记录当前位置
################这边对于last_position,next_position,current_position的计算方法需要大改############
    for i in range(50):
        current_possition += .point[i][MainWindow.time] + ',' + MainWindow.point[i][MainWindow.time + 1] + ','
    next_possition = current_possition + last_position
    # print(MainWindow.gps_now)
#################### 第2次使用.emit传递变量 ############################
    MainWindow.interact_obj.sig_send_to_js.emit(next_possition)
    
    ## 标记一下初始位置
    if MainWindow.time == 0:
        print('初始位置：')
        print(current_position)
    
    ## 用于表示时间的流逝
    MainWindow.time +=2
    
################## d是什么变量？感觉这段代码毫无用处呀##################
    if d <= MainWindow.time:
        MainWindow.timer.stop()
######################第3次使用.emit传递变量###################
        MainWindow.interact_obj.sig_send_to_js.emit('shuaxin')
        
    @pyqtSlot()
    ##  '同步到Web'按钮
    def on_pushButton_clicked():  #回调函数、解耦
        # 这个信号是在js中和一个js方法绑定的,所以发射这个信号时会执行对应的js方法.
        self.interact_obj.sig_send_to_js.emit('-1,' + str(self.qi0[0][1:-1]))
        # self.textBrowser.clear()  # 调试程序，用来清除文本框
        
    @pyqtSlot()
    ## '确定'按钮
    def on_pushButton2_clicked():   #传入的是速度，按钮对应“确定”
        ## 接收textEdit文本框中的文字，并保存在text中，类型变换为int后保存在speed中
        text = self.textEdit_2.toPlainText()
        global speed
        speed = int(text)