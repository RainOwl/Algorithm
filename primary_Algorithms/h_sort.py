#_author_ : duany_000
#_date_ : 2018/3/12
import random
from 算法 import a_sort

data_set = list(range(10))
random.shuffle(data_set)

def shft(data_set, low, high):
    i = low  # 父节点
    j = 2*i+1  # 左孩子下标
    temp = data_set[i]
    while j<=high:
        if j < high and data_set[j] < data_set[j+1]:  # 存在右孩子，且左孩子小于右孩子
            j += 1  # 取右孩子位置，较大的值
        if temp < data_set[j]:         # 孩子节点的值大于父节点
            data_set[i] = data_set[j]  # 取孩子节点较大的值放在父节点
            i = j
            j = 2*i + 1
        else:
            break
    data_set[i] = temp  # 将原父节点的值放入调整的子节点位置

@a_sort.cal_time
def heap_sort(data_set):
    n = len(data_set)   # data_set = [0,2,3,4,5,6,7,8,9,1]
    for i in range(n//2,-1,-1):  # 完全二叉树的最后一个节点的下标，生成下标列表【4,3,2,1,0】，从小堆开始局部调整
        shft(data_set,i,n-1)
    for i in range(n-1,-1,-1):   # 【9,8,...,0】
        data_set[0],data_set[i] = data_set[i],data_set[0]
        shft(data_set,0,i-1)


data_set = list(range(10))
random.shuffle(data_set)
heap_sort(data_set)

