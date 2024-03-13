import numpy as np
import random
import re


class ChargingPile:
    def __init__(self,charging_pile_id,order_id,arrival_time,start_time,finish_time,charging_capacity,charging_cost,code):
        self.pile_id = charging_pile_id
        self.order_id = order_id
        self.A_time = arrival_time
        self.S_time = start_time
        self.F_time = finish_time
        self.capacity = charging_capacity
        self.cost = charging_cost
        self.code = code
        self.array_data = None


    # def receive_order(self):
    #     pass
    #
    # def address(self):
    #     interval_x = [106.61000, 106.61999]
    #     interval_y = [29.53000, 29.53999]
    #
    #     #随机生成区间内的十组地址数组
    #     random_array_x = np.round(np.random.uniform(interval_x[0], interval_x[1], 10),5)
    #     random_array_y = np.round(np.random.uniform(interval_y[0], interval_y[1], 10),5)
    #     address_array = [val for pair in zip(random_array_x, random_array_y) for val in pair]
    #
    #     print("地址数组：",address_array)
    #
    # def charging(self):
    #     #随机生成充电电量，计算花费
    #     charge_power = np.round(random.uniform(0, 100),3)
    #     #取每度电单价1.5元
    #     cost = charge_power * 1.5
    #
    #     print("充电电量（度）：",charge_power)
    #     print("充电花费(元）：",cost)


    # 读取数据和储存
    def read_and_store_array_data(self):
        pattern = r'\[([^]]+)\]'  # 正则表达式模式，匹配方括号内的内容
        match = re.search(pattern, self.code)  # 在代码中搜索匹配的内容

        if match:
            array_data_str = match.group(1)  # 获取匹配到的内容
            array_data = [float(x.strip()) for x in array_data_str.split(',')]  # 分割字符串并转换为浮点数列表
            self.array_data = np.array(array_data)
        else:
            self.array_data = None

        print(self.array_data)  # 打印获取到的数据组


code = """self.post_ = np.array(
            [106.615559, 29.538386, 106.612811, 29.535215, 106.61803, 29.536547, 106.612397, 29.546053, 106.615704,
             29.537384, 106.611434, 29.535636, 106.612279, 29.538397, 106.610106, 29.533026, 106.613436, 29.540303,
             106.616361, 29.535254, 106.618242, 29.532338, 106.609128, 29.540774, 106.610177, 29.535436])"""
pile001 = ChargingPile(1,1,1,1,1,1,1,code)
#pile001.address()
#pile001.charging()
pile001.read_and_store_array_data()


