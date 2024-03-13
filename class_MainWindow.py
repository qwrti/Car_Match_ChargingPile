import os

import numpy as np
from PyQt5.QtCore import QUrl, pyqtSlot, QObject, pyqtSignal, QTimer
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow

from Ui_main import Ui_MainWindow

Cycle_Index = 50
Car_Num = 1
Pile_Num = 10

d = 50

REMAIN = 5
LAB = -1  # 判断是否确定速度标志位

'''定义寻找最近点的函数。这里是算法所需要修改的重点部分'''


def generate_random_num():  # 随机产生1或-1
    n = np.random.rand()
    if n >= 0.5:
        return 1
    if n < 0.5:
        return -1


def coo(x, x2, xx, xx2):
    right = []
    x1 = np.array(x)
    xx1 = np.array(xx)
    x3 = np.array(x2)
    xx3 = np.array(xx2)
    for i in range(len(x1)):
        l = abs(x1 - xx1[i])  # 求出x1全体对xx1某值的差值
        position = np.where(l == min(l))[0]
        l2 = abs(x3 - xx3[i])  # 求出x3全体对xx3某值的差值
        position2 = np.where(l2 == min(l2))[0]
        p = [i for i in position if i in position2]  # 查找相同值
        if len(p) != 0:
            p0 = p[0]
            right.append(p0)  # p有值则填入right
            x1[p0] = 0
            x3[p0] = 0
        if len(p) == 0:
            p0 = 0
            right.append(p0)
    # print(right)
    return right


'''重点修改的部分 '''


def find_shortest_path_simple(p1, p2, v):  # 寻找某点到V最短距离
    # p1保存了所有起点的经度，p2保存了所有起点的纬度
    # v "0,2"等位置保存经度，“1，3”等位置保存维度
    res = 100
    num = -1

    for i in range(0, len(v), 2):
        distance = (p1 - v[i]) ** 2 + (p2 - v[i + 1]) ** 2
        if distance < res:
            res = distance
            num = i
    # print(num)
    return res, num


# start_longitude是起点经度，start_latitude是起点维度，起点只有一个；destinaiton是数组，destinaiton[单数]是终点经度，
# destinaiton[单数+1]是该终点对应的纬度
def Dijsra(start_longitude, start_latitude, destination):  # 图论分析法
    pass


def DRL_method(start, destination):  # 基于 DＲL 方法的电动汽车充电导航模型
    pass


def DQN_method(start, destination):  # 基于 DQN 方法的电动汽车充电导航模型
    pass


# v相当于route_p。保证route_p的数据长度为l
def normlization(v, l):
    if len(v) > l:
        return v[:l]
    if len(v) < l:
        for i in range(l - len(v)):
            v.append(v[-2])
        return v


def gai():
    n = np.random.rand()
    if n >= 0.5:
        return 1
    if n < 0.5:
        return -1


# 回调函数用于处理从JavaScript接收到的数据
class TInteractObj(QObject):
    sig_send_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 交互对象接收到js调用后执行的回调函数.
        self.receive_str_from_js_callback = None

    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        self.receive_str_from_js_callback(str)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.count = Cycle_Index
        self.last_p = []
        text = self.textEdit.toPlainText()
        print(text)
        self.gps_qidian = []
        self.car_c = np.ones([Car_Num], dtype=np.uint8) * (-1)

        # post定义了充电桩的位置
        self.post = '106.615559,29.538386,106.612811,29.535215,106.61803,29.536547,106.612397,29.546053,106.615704,' \
                    '29.537384,106.611434,29.535636,106.612279,29.538397,106.610106,29.533026,106.613436,29.540303,' \
                    '106.616361,29.535254,106.618242,29.532338,106.609128,29.540774,106.610177,29.535436'
        self.post_ = np.array(
            [106.615559, 29.538386, 106.612811, 29.535215, 106.61803, 29.536547, 106.612397, 29.546053, 106.615704,
             29.537384, 106.611434, 29.535636, 106.612279, 29.538397, 106.610106, 29.533026, 106.613436, 29.540303,
             106.616361, 29.535254, 106.618242, 29.532338, 106.609128, 29.540774, 106.610177, 29.535436])
        self.post_num = np.ones([26], dtype=np.uint8)
        self.point = []
        self.power = np.random.rand(Car_Num) * 0.7 + 0.3  # 函数返回一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1。
        self.index = (os.path.split(os.path.realpath(__file__))[0]) + "/index.html"
        self.webview.load(QUrl.fromLocalFile(self.index))
        self.init_channel()
        self.qi = np.array([106.614248, 29.53727]) + (
                np.random.rand(Car_Num, 2) - 0.5) / 100  # ‘50’限制产生的起点数量。‘106.614248, 29.53727’限制起点的位置
        self.qi0 = list(map(str, self.qi.reshape(1, -1).tolist()))  ## 讲qi转换成传给index.html的文件
        self.noword = 0

    # =============================================================================
    #         print(self.qi0[0][1:-1])
    # =============================================================================
    # =============================================================================
    #         self.interact_obj.sig_send_to_js.emit('-1,'+self.qi0[0][1:-1])
    # =============================================================================
    def init_channel(self):

        self.interact_obj = TInteractObj(self)
        self.interact_obj.receive_str_from_js_callback = self.receive_data

        channel = QWebChannel(self.webview.page())
        # interact_obj 为交互对象的名字,js中使用.
        channel.registerObject("interact_obj", self.interact_obj)

        self.webview.page().setWebChannel(channel)

    def receive_data(self, data):
        # =============================================================================
        print(data)
        # =============================================================================
        self.last_p = []
        self.point = []
        self.l = 0
        self.time = 0
        ############## data=-1的时候，是在做初始化 ################
        if data[0] == '-' and data.count(',') == 101:  ## 一个逗号表示一对坐标，共计50个起点
            self.interact_obj.sig_send_to_js.emit(data[1:])  # 第一次定位”1，“
            self.gps_qi = data[1:].split(',')[1:-1]  # data数据将其加到gps_qi
            self.gps_zhong = list(map(float, self.gps_qi))  # 转为浮点数
            self.gps_qidian = self.gps_zhong.copy()  # gps_qidian为gps_zhong异名同体
            # print(self.gps_zhong)

            for i in range(len(self.gps_zhong)):
                self.gps_zhong[i] += (np.random.rand() - 0.5) / 500 + gai() * 0.001  # 随机化按规则范围随机化gps_zhong
            # print(len(self.gps_zhong), self.gps_zhong)
            self.gps_zhong1 = list(map(str, self.gps_zhong))  # gps_zhong1为字符串类型
            self.gps_zhong0 = ",".join(self.gps_zhong1)  # 在gps_zhong1中间加入，为gps_zhong0

            self.qizhong = "0," + data[3:] + self.gps_zhong0  # qizhong为0，+data[3:]（起点）+ self.gps_zhong0（终点）

            self.interact_obj.sig_send_to_js.emit(self.qizhong)
            self.noword += 1

        # 对车进行判断
        if data == 'shuaxin':
            # =============================================================================
            #
            # =============================================================================

            self.gps_qi = self.gps_now.split(',')[1:-1]
            self.power_change = [False] * Car_Num

            self.gps_zhong = list(map(float, self.gps_qi))  # gps_zhong化为浮点数
            self.gps_qidian = self.gps_zhong.copy()  # gps_qidian为gps_zhong异名同体
            # =============================================================================
            #             print('this is gps_zhong')
            #             print(self.gps_zhong)
            #             print('this is gps_zhong........................\n')
            # =============================================================================

            # self.gps_zhong_copy=self.gps_zhong.copy()
            # =============================================================================
            #             print(self.gps_now)
            # =============================================================================

            for i in np.where(self.power >= 0.7)[0]:
                if self.car_c[i] != -1:
                    self.car_c[i] = -1

            for i in range(len(self.gps_zhong)):
                self.gps_zhong[i] += (np.random.rand() - 0.6) / 300 + gai() * 0.002  # 车有电的时候，就随机找一个终点

            # print(self.gps_zhong)
            # 车没电的时候，就找一个最近的充电桩
            for i in np.where(self.power <= 0.2)[0]:
                # 表示没充好电，就保持目的地为上一个循环中保存的充电桩位置
                if self.car_c[i] != -1:
                    self.gps_zhong[2 * i] = self.post_[self.car_c[i]]
                    self.gps_zhong[2 * i + 1] = self.post_[self.car_c[i] + 1]

                    # print("car_c[i] != -1")
                if self.car_c[i] == -1:  # -1表示“否”
                    # print(self.post_num)
                    _, num = find_shortest_path_simple(self.gps_qidian[2 * i], self.gps_qidian[2 * i + 1],
                                                       self.post_)  # 找到需要到的点, **有删改   num表示充电桩的编号
                    self.car_c[i] = num  # 把充电桩的编号给数组，保存车辆的目的地
                    # self.post_num[num] = 0
                    # self.post_num[num + 1] = 0
                    self.gps_zhong[2 * i] = self.post_[num]
                    self.gps_zhong[2 * i + 1] = self.post_[num + 1]

            # print((np.array(ces)-np.array(self.gps_zhong),))

            self.gps_zhong1 = list(map(str, self.gps_zhong))
            # 应该对的起点是self.qidian ,self.zhong
            # 返回的路径
            # =============================================================================
            #             print(self.gps_zhong1)
            # =============================================================================
            self.gps_zhong0 = ",".join(self.gps_zhong1)
            # =============================================================================
            #             print('这是终点')
            #             print(self.gps_zhong1)
            # =============================================================================
            ###########  “0，”表示要显示路径 ##############
            self.qizhong = "0," + self.gps_now[2:] + self.gps_zhong0
            # =============================================================================
            #             print(self.qizhong)
            # =============================================================================

            self.interact_obj.sig_send_to_js.emit(self.qizhong)
        # data=1是在画完路径后data里面保存了路径（一堆点连成了一条线）
        if data[0:2] == "1," and data.count('\n') == 50:

            self.route = data[2:].split('\n')[:-1]

            self.route_p = []
            for i in self.route:
                self.route_p.append(i.split(',')[:-1])
            for i in self.route_p:
                # =============================================================================
                #                 if len(i)<self.l:
                #                     self.l=len(i)
                # =============================================================================
                self.l += len(i)
            self.l /= 50
            self.l = int(self.l)  # l为均长
            # print(self.l)
            cuoqi = []
            cuozhong = []
            self.last = []
            for i in range(len(self.route_p)):
                cuoqi.append(float(self.route_p[i][0]))  # 保存经度坐标

            for i in range(len(self.route_p)):
                cuozhong.append(float(self.route_p[i][-2]))  # 保存最后一个点的经度坐标
            right = coo(cuoqi, cuozhong, self.gps_qidian[::2], self.gps_zhong[::2])

            print('电量：：：：：')
            print(self.power)
            print('当前速度', speed)
            print('当前速度电量减少量', power_reduce)
            # print(self.power_change)

            for i in range(50):
                if (self.car_c[i] == -1):  ## 没充上电，电量要继续减少
                    self.power[i] -= power_reduce
                # 遇到充电桩
                else:
                    if self.power[i] >= 0.7:  # 电量足够，不充了
                        pass
                    else:
                        self.power[i] += 0.3  # 充电，电量上升

            r = right.copy()
            r.sort()

            if (np.array(r) - np.arange(50)).any() == 0:  # arange函数用于创建等差数组
                for i in right:
                    # tiaojie(self.route_p[i], step)
                    self.last.append()
                # print('np.array(r) - np.arange(50)')

                # print('这是之后的数据', self.last)
                for i in range(len(self.route_p)):
                    # tiaojie(self.last[i], step)
                    self.point.append(normlization(self.last[i], d))
                # print(self.route_p)
                # print(self.point)
            # =============================================================================
            else:
                # print('这是之前的数据',  len(self.route_p), self.route_p)
                # print('这是之后的数据', self.route_p)
                for i in range(50):
                    # tiaojie(self.route_p[i],  count[i])
                    # print ('self.route_p[i]',self.route_p[i])
                    self.point.append(normlization(self.route_p[i], d))
                # print('这是之后的数据', len(self.point), self.point)

            for i in range(50):
                if self.point[i] == None:
                    self.point[i] = []
                    for j in range(d):
                        self.point[i].append(str(self.gps_qidian[2 * i]))
                        self.point[i].append(str(self.gps_qidian[2 * i + 1]))
            self.timer = QTimer(self)  # 初始化一个定时器

            if self.time < d:  # self.l:
                self.timer.timeout.connect(self.run)
                self.timer.start(timer2)  # 设置计时间隔并启动

            if d <= self.time:
                self.timer.stop()
                self.gps_qi = self.gps_now.split(',')[1:-1]
                self.gps_zhong = list(map(float, self.gps_qi))
                for i in range(len(self.gps_zhong)):
                    self.gps_zhong[i] += (np.random.rand() - 0.5) / 300 + gai() * 0.002
                self.gps_zhong = list(map(str, self.gps_zhong))
                self.gps_zhong0 = ",".join(self.gps_zhong)
                self.qizhong = "0," + data[3:] + self.gps_zhong0

                self.interact_obj.sig_send_to_js.emit(self.qizhong)

    def run(self):
        self.gps_now = '1,'
        for i in range(50):
            # self.gps_now+=self.route_p[i][self.time]+','+self.route_p[i][self.time+1]+','
            self.gps_now += self.point[i][self.time] + ',' + self.point[i][self.time + 1] + ','
        self.gps_now1 = self.gps_now + self.post
        # print(self.gps_now)
        self.interact_obj.sig_send_to_js.emit(self.gps_now1)
        # =============================================================================
        #         if self.time==0:
        #             print('这是第一次')
        #             print(self.gps_now)
        # =============================================================================
        self.time += 2  ## 一直加到比d=50大，然后进行刷新,地图里的点会动50/2次

        if d <= self.time:
            self.timer.stop()
            self.interact_obj.sig_send_to_js.emit('shuaxin')

    @pyqtSlot()
    def on_pushButton_clicked(self):

        if LAB == 1:
            ## 刚跑程序时，初始化起点##
            self.interact_obj.sig_send_to_js.emit('-1,' + str(self.qi0[0][1:-1]))
        else:
            return

    @pyqtSlot()
    def on_pushButton2_clicked(self):
        global LAB
        LAB = 1
        text = self.textEdit.toPlainText()
        global speed
        if (text.isdigit() and int(text) > 1):
            speed = int(text)
        else:
            speed = 1000
            # 单位米/秒
        if (speed < 1200 and speed > 30):
            global timer2
            timer2 = round(-16 / 19 * speed + 1042)
        else:
            timer2 = 500
        # 电量速度关系式
        global power_reduce
        power_reduce = -1 * speed * 6 / 1000000
