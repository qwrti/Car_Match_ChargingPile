import numpy as np
import re

class Car:
    def __init__(self,parent = None):
        ######## 只保留 可以赋值的那些变量
        self.car_id = []
        self.trip_id = []
        self.time = []
        self.coordinate = []
        self.soc = []
        self.speed = []
        self.code_qi = []
        self.code_zhong = []
        self.qi_array_data = []
        self.zhong_array_data = []

    def qi_read_and_store_array_data(self):
        pattern = r'\[([^]]+)\]'  # 正则表达式模式，匹配方括号内的内容
        match = re.search(pattern, self.code_qi)  # 在代码中搜索匹配的内容

        if match:
            array_data_str = match.group(1)  # 获取匹配到的内容
            array_data = [float(x.strip()) for x in array_data_str.split(',')]  # 分割字符串并转换为浮点数列表
            self.qi_array_data = np.array(array_data)
        else:
            self.qi_array_data = None

        print(self.qi_array_data)  # 打印获取到的数据组

    # 读取终点坐标
    def zhong_read_and_store_array_data(self,gps_qi):
        start = gps_qi
        
        pattern = r'\[([^]]+)\]'  # 正则表达式模式，匹配方括号内的内容
        match = re.search(pattern, self.code_zhong)  # 在代码中搜索匹配的内容

        if match:
            array_data_str = match.group(1)  # 获取匹配到的内容
            array_data = [float(x.strip()) for x in array_data_str.split(',')]  # 分割字符串并转换为浮点数列表
            self.zhong_array_data = np.array(array_data)
        else:
            self.zhong_array_data = None

        print(self.zhong_array_data)  # 打印获取到的数据组

code_qi = '''self.post_ = np.array(
            [106.615559, 29.538386, 106.612811, 29.535215, 106.61803, 29.536547, 106.612397, 29.546053, 106.615704,
             29.537384, 106.611434, 29.535636, 106.612279, 29.538397, 106.610106, 29.533026, 106.613436, 29.540303,
             106.616361, 29.535254, 106.618242, 29.532338, 106.609128, 29.540774, 106.610177, 29.535436])'''
code_zhong = '''self.post_ = np.array(
            [106.615559, 29.538386, 106.612811, 29.535215, 106.61803, 29.536547, 106.612397, 29.546053, 106.615704,
             29.537384, 106.611434, 29.535636, 106.612279, 29.538397, 106.610106, 29.533026, 106.613436, 29.540303,
             106.616361, 29.535254, 106.618242, 29.532338, 106.609128, 29.540774, 106.610177, 29.535436])'''
car001 = Car(1,1,1,1,1,1,code_qi,code_zhong)
#car001.start_address()
#car001.destination_address()
car001.qi_read_and_store_array_data()
car001.zhong_read_and_store_array_data()