import numpy as np

def generate_random_num(): # 随机产生1或-1
    n = np.random.rand()
    if n >= 0.5:
        return 1
    if n < 0.5:
        return -1

#################  重点修改的部分 ##################
def find_shortest_path_simple(p1, p2, v):  # 寻找某点到V最短距离
    res = 100
    num = -1

    for i in range(0, len(v), 2):
        distance = (p1 - v[i]) ** 2 + (p2 - v[i + 1]) ** 2
        if distance < res:
            res = distance
            num = i
    # print(num)
    return res, num

############### v相当于route_p。保证route_p的数据长度为l ##############
def normlization(v, l):
    if len(v) > l:
        return v[:l]
    if len(v) < l:
        for i in range(l - len(v)):
            v.append(v[-2])
        return v