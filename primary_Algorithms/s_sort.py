#_author_ : duany_000
#_date_ : 2018/3/12
import time
import random

def cal_time(func):
    def inner(*args, **kwargs):
        s_time = time.time()
        r = func(*args, **kwargs)
        e_time = time.time()
        print("spend time>>>", e_time-s_time)
        return r
    return inner

@cal_time
def shell_sort(li):
    gap = len(li)//2
    while gap >= 1:
        for i in range(gap,len(li)):
            temp = li[i]
            j = i-gap
            while j >= 0 and temp <= li[j]:
                li[j+gap] = li[j]
                j -= gap
            li[j+gap] = temp
        gap //= 2

data_set = list(range(100000))
random.shuffle(data_set)

shell_sort(data_set)