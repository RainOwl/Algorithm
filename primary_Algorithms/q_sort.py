#_author_ : duany_000
#_date_ : 2018/3/12
import copy
import random
from 算法 import a_sort


def _quick_sort(data_set, left, right):
    if left < right:
        mid = partition(data_set, left, right)
        # print("left, right",left, right)
        _quick_sort(data_set,left,mid-1)
        _quick_sort(data_set,mid+1,right)

def partition(data_set, left, right):
    temp = data_set[left]
    while left < right:
        while left < right and temp <= data_set[right]:
            right -= 1
        data_set[left] = data_set[right]
        while left < right and temp >= data_set[left]:
            left += 1
        data_set[right] = data_set[left]
    data_set[left] = temp
    return left

@a_sort.cal_time
def quick_sort(data_set):
    return _quick_sort(data_set, 0, len(data_set)-1)

data_set = list(range(10))
random.shuffle(data_set)

quick_sort(data_set)



