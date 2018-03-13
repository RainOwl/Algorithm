#_author_ : duany_000
#_date_ : 2018/3/13
import random

data_set = []
for i in range(100):
    data_ra = random.randint(0, 100)
    data_set.append(data_ra)

"""
问题：现在有一个列表，列表中的数范围都在0到100之间，列表长度大约为100万。
设计算法在O(n)时间复杂度内将列表进行排序。
"""
def count_sort(li, max_num):
    count = [0 for i in range(max_num+1)]
    for num in li:
        count[num] += 1

    ini = 0
    for num,co in enumerate(count):
        print("num,co>>>",num,co)
        for j in range(co):
            li[ini]=num
            ini += 1
    return li

# print(count_sort(data_set,100))
#################################

"""
现在有n个数（n>10000），设计算法，按大小顺序得到前10大的数。
1、插入排序法--insert_sort、topk
2、堆排序
"""


def insert_sort(li):
    for i in range(1,len(li)):
        j = i-1
        while j>= 0 and li[i] < li[j]:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = li[i]
    return li

def topk(li, k):
    temp = [0 for i in range(k+1)]   # [0,0,0,*] k=3
    temp[0:k] = li[0:k]                  # [5,0,0,*]
    insert_sort(temp)
    for i in range(k,len(li)):
        j = len(temp)-2   #j = 5-2=3  倒数第二个位置
        while j >= 0 and temp[j] > li[i]:
            temp[j+1] = temp[j]
            j -= 1
        temp[j+1] = li[i]
        # print(temp)
    return temp

data = list(range(10))
random.shuffle(data)
print(data)
print("---------------------")
# print(topk(data, 10))

#################################

def shft(data_set, low, high):
    i = low  # 父节点
    j = 2*i+1  # 左孩子下标
    temp = data_set[i]
    while j<=high:
        if j < high and data_set[j] > data_set[j+1]:
            j += 1  # 取右孩子位置，较小的值
        if temp > data_set[j]:         # 孩子节点的值小于父节点
            data_set[i] = data_set[j]  # 取孩子节点较小的值放在父节点
            i = j
            j = 2*i + 1
        else:
            break
    data_set[i] = temp  # 将原父节点的值放入调整的子节点位置

def topn(li,k):
    heap = li[0:k]
    # 建堆：小根堆
    for i in range(k//2-1,-1,-1):
        shft(heap, i, k-1)
    # print("heap1>>>",heap)
    # 遍历：比根节点小的直接剔除
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            shft(heap, 0, k-1)
    # print("heap2>>>", heap)
    # 展示数据
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        shft(heap, 0, k-1)
    return heap

print(topn(data,5))



