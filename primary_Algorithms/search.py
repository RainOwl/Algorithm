#_author_ : duany_000
#_date_ : 2018/3/12
import time
"""
[1,2,3,4,5,6,8,9,12,33,35,38,39,41,43,46,48,51,53]
"""
def _binary_search(data_set, val):
    low = 0
    high = len(data_set)-1
    while low <= high:
        mid = (high+low)//2 #  取整
        if val==data_set[mid]:
            return mid
        elif val < data_set[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return

def cal_time(func):
    def inner(*args, **kwargs):
        s_time = time.time()
        r = func(*args, **kwargs)
        e_time = time.time()
        print("spend time>>>",e_time-s_time)
        return r
    return inner


# 递归函数不宜直接使用装饰器
@cal_time
def binary_search(data_set, val):
    return _binary_search(data_set, val)

data_set = list(range(10000000))
res = binary_search(data_set, 896)
print(res)

# def linear_search(data_set, value):
#     for i in data_set:
#         if data_set[i] == value:
#             return i
#     return
#
# l_res = linear_search(data_set,749)
# print(l_res)