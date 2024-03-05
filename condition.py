import numpy as np
################### 设置经纬度 #######################
# 要求经、纬度必须成对，否则会出现错误
def sep(a):  # 对目标点确定间隔,用均值/划分次数计算
    #这个函数再"tiaojie"函数中调用
    c = []
    for i in range(1, len(a)):
        c.append(abs(a[i] - a[i - 1]))
    return c
def tiaojie(List_random, con_sep):
    list_heng = []
    list_zong = []
    List_out = []
    print(List_random)
    i = -1
    while i+1 < len(List_random):
        i += 1
        if i % 2 == 0:
            if (i > 2 and List_random[i] == List_random[i - 2]):
                list_heng.append(List_random[i] + 0.1**(REMAIN-2))
            else:
                list_heng.append(List_random[i])
        else:
            if (i > 1 and List_random[i] == List_random[i - 2]):
                list_zong.append(List_random[i] + 0.1**(REMAIN-2))
            else:
                list_zong.append(List_random[i])
    List_sep = sep(list_heng)
    List_sep2 = sep(list_zong)
    print(con_sep)
    for j in range(0, len(List_sep)):
        List_out.append(list_heng[j])
        List_out.append(list_zong[j])
        scale = round(List_sep[j]/List_sep2[j], 4)
        local = list_heng[j]
        local2 = list_zong[j]
        while (1):
            if(abs(local2 - list_zong[j+1]) < con_sep):
                break
            else:
                local2 = round(local2 + (list_zong[j+1]-list_zong[j])/abs(list_zong[j+1]-list_zong[j])*con_sep, REMAIN)
                local = round(local+(list_heng[j+1]-list_heng[j])/abs(list_heng[j+1]-list_heng[j])*con_sep*scale, REMAIN)
                List_out.append(local)
                List_out.append(local2)
    if (List_random[-2] != List_out[-2] or List_random[-1] != List_out[-1]):
        List_out.append(List_random[-2])
        List_out.append(List_random[-1])
    print(List_out)
    return List_out

#################### 寻找某点到V最短距离 ###################
def find_n(p1, p2, v):  
    res = 100
    num = -1

    for i in range(0, len(v), 2):
        distance = (p1 - v[i]) ** 2 + (p2 - v[i + 1]) ** 2
        if distance < res:
            res = distance
            num = i
    # print(num)
    return res, num