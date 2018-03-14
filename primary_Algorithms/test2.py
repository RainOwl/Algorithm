#_author_ : duany_000
#_date_ : 2018/3/14
import copy

"""
给定一个升序列表和一个整数，返回该整数在列表中的下标范围。
"""
data_set = [1,2,2,2,3,3,4,4,4,4,5,5,7,8,8,9,10]

def binary_search(data_set, val):
    low = 0
    high = len(data_set)-1
    temp = []
    while low <= high:
        mid = (high+low)//2 #  取整
        if val==data_set[mid]:
            left = mid
            right = mid
            while right+1 < len(data_set) and data_set[right+1]==val:
                right += 1
            while left-1 >= 0 and data_set[left-1]==val:
                left -= 1
            return left,right
        elif val < data_set[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return temp

# print(binary_search(data_set, 4))
###############################################
"""
给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数。保证肯定仅有一个结果。
"""
li = [1,3,6,2,7]
target = 5

def func1(li,target):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i]+li[j]==target:
                return i,j
    return

# print(func1(li,target))
################方法一end##################

def _binary_search(data_set, val, low, high):
    # low = 0
    # high = len(data_set)-1
    while low <= high:
        mid = (high+low)//2 #  取整
        if val==data_set[mid]:
            return mid
        elif val < data_set[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return

def func2():
    li_temp = copy.deepcopy(li)
    li_temp.sort()
    for i in range(len(li_temp)):
        a = i
        b = _binary_search(li_temp, target-li_temp[i], i+1, len(li_temp)-1)
        if b:
            return li.index(li_temp[a]),li.index(li_temp[b])
    return

# print(func2())


