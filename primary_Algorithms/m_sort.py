# _author_ : duany_000
# _date_ : 2018/3/12
import random
import time
import sys

def cal_time(func):
    def inner(*args, **kwargs):
        s_time = time.time()
        r = func(*args, **kwargs)
        e_time = time.time()
        print("spend time>>>", e_time-s_time)
        return r
    return inner

def merger_sort(li, low, high):
    if low < high:
        mid = (high - low) // 2
        merger_sort(li, low, mid)
        merger_sort(li, mid + 1, high)
        merger(li, low, mid, high)


def merger(li, low, mid, high):
    i = low
    j = mid + 1
    temp_list = []
    while i <= mid and j <=high:
        if li[i] <= li[j]:
            temp_list.append(li[i])
            i += 1
        else:
            temp_list.append(li[j])
            j += 1
    while i <= mid:
        temp_list.append(li[i])
        i += 1
    while j <= high:
        temp_list.append(li[j])
        j += 1

    li[low:high+1] = temp_list

@cal_time
def _merger_sort(li):
    return merger_sort(li, 0, len(li)-1)

sys.setrecursionlimit(100000)

data_set = list(range(100000))
random.shuffle(data_set)

_merger_sort(data_set)


