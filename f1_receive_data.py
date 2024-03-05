################## Receive_data方法本来是在MainWindow类内部的，所以可以直接用self。现在MainWindow和receive_data在两个py文件中，我应该怎么让程序正常运行呢？ ###################
from PyQt5.QtCore import QTimer
from class_MainWindow import MainWindow
################ 导入自己写的函数，这一句代码是否有误 #####################
from f2_find_shortest_path import normlization,find_shortest_path,generate_random_num
from button_function import run
cycle_index = 50 #循环次数，用于定义for循环的次数
## f1是function 1(功能1)的意思
##################### Last_p,point,l,time分别代表什么？###########################
def receive_data(data):
    # =============================================================================
    print(data)  #输出在应用界面的文本框中输入的数据。这里data就是speed速度
    # =============================================================================
    #私有变量定义
########################  If语句里的判断条件，事实上是在判断什么呢？ ###############################
    if data[0] == '-' and data.count(',') == 101:
        MainWindow.interact_obj.sig_send_to_js.emit(data[1:])  # 第一次定位'1,'

        gps_qi = data[1:].split(',')[1:-1]  # data数据将其加到gps_qi
        gps_destination = list(map(float, self.gps_qi))  # 转为浮点数
        self.gps_start = self.gps_destination.copy()  # gps_start为gps_destination异名同体
        # print(self.destination)
        
        #destination1和destination2分别是什么含义呢？
        for i in range(len(self.gps_destination)):
            gps_destination[i] += (np.random.rand() - 0.5) / 500 + generate_random_num() * 0.001  # 随机化按规则范围随机化gps_destination
        # print(len(self.gps_destination), self.gps_destination)
        
        gps_destination1 = list(map(str, self.gps_destination))  # gps_destination1为字符串类型
        gps_destination0 = ",".join(self.gps_destination1)  # 在gps_destination1中间加入，为gps_destination0
        qidestination = "0," + data[3:] + self.gps_destination0  # qidestination为0，+data[3:]+ self.gps_destination0
        
        # qizhong是什么含义？
        MainWindow.qizhong = "0," + data[3:] + gps_destination0
########################### 第一次使用.emit传递变量 ###############################
        MainWindow.interact_obj.sig_send_to_js.emit(MainWindow.qizhong)
        
###################### 判断条件在判断什么呢？感觉这一段判断语句的内部，可以全部都直接删掉##########################
    if data == 'shuaxin':
        pass
    
###################### 判断条件在判断什么呢？##########################
    if data[0:2] == "1," and data.count('\n') == 50:
        temp = data[2:].split('\n')[:-1] #temp只是个中间变量
        route = []
        for i in temp:
            route.append(float(route[i][0]))
        for i in route:
            MainWindow.l = MainWindow.l + len(i)
        MainWindow.l =MainWindow.l/50
        
        print(MainWindow.l)           
############## cuoqi,cuozhong两个变量存储了什么呀，看不懂 ################
        cuoqi=[]
        cuozhong=[]
        last=[]
        for i in range(len(route)):
            cuoqi.append(float(route[i][0]))
            cuozhong.append(float(route[i][-2]))
        
        final_route = find_shortest_path((cuoqi, cuozhong,gps_start[::2], gps_destination[::2]))
        print ('当前速度',speed)
        
        final_route_sort = final_route.copy()
        final_route_sort.sort()
############### last,point这两个变量是什么含义?d这个变量的含义太迷惑了,在源代码种也是一个恒为50的数。所以我将它改为cycle_index了 ######################
    if (np.array(final_route_sort) - np.arange(50)).any() == 0: # # arange函数用于创建等差数组
        for i in final_route:
            last.append()
        
        for i in range(len(route)):
            point.append(normlization(last[i],cycle_index))
    else:
        for i in range(50):  # 为什么这段我要循环50次，往上提会发生准确性的变化吗？
            point.append(normlization(route[i],cycle_index))
    
    for i in range(cycle_index): #这里也是同理，会有什么变化?
        if point[i] == None:
            point[i] = []
            for j in range(cycle_index):
                point_append(normlization(route[i],cycle_index))
            
################ 这里在point后面加上gps_start[2 * i]，gps_start[2 * i+1]，用于 ##############
    for i in range(cycle_index):
        if point[i] == None:
            point[i] = []
            for j in range(d):
                point[i].append(str(gps_start[2 * i]))
                point[i].append(str(gps_start[2 * i + 1]))
                timer = QTimer()  # 初始化一个定时器
############ time感觉就是循环次数的意思。但timer变量是什么含义呢？ ############
    if time < cycle_index: # 如果循环次数还没有达标
        timer.timeout.connect(run)
        timer.start(500) # 这里的500是什么意义呢？感觉应该改成我所需要的内容
    else: # 已达到提前设置的循环次数
        timer.stop()
        gps_start=gps_now.split(',')[1:-1]
        gps_destination = list(map(float,gps_start))
        for i in range(len(gps_destination)):
            gps_destination[i] += (np.random.rand() - 0.5) / 300 + generate_random_num() * 0.002  #随机产生终点，这里以后肯定要修改
            gps_destination = list(map(str, gps_destination))
            gps_destination0 = ",".join(gps_destination)
            MainWindow.qizhong = "0," + data[3:] + gps_destination0
            MainWindow.interact_obj.sig_send_to_js.emit(MainWindow.qizhong)