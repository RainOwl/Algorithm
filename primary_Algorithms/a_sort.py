#_author_ : duany_000
#_date_ : 2018/3/12
import random
import time

def cal_time(func):
    def inner(*args, **kwargs):
        s_time = time.time()
        r = func(*args, **kwargs)
        e_time = time.time()
        print("spend time>>>", e_time-s_time)
        return r
    return inner

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):  # 总共遍历len(li)-1次,倒数第二次已得到最终结果
        exchange = False
        for j in range(len(li)-i-1):
            while li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break

data = list(range(10000))
random.shuffle(data)  #  打乱排序


# bubble_sort(data)
#################bubble_sort end##################


@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):  # 循环最小位置的后一个，直到最后一个值
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]

# select_sort(data)
##################select_sort end################


@cal_time
def insert_sort(li):
    for i in range(1,len(li)):
        # temp = li[i]
        j = i - 1 # i前一位
        while j>=0 and li[j]>li[i]:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = li[i] # 最终到第0个位置


# insert_sort(data)
##############insert_sort end################

"""
生成数据
[
{id:1000,name:ll,age:18},
{id:1001,name:ll,age:18},
{id:1002,name:ll,age:18},
]
查询某个id,显示此人信息
"""
def random_list(n):
    data_set = []
    ids = list(range(1000,1000+n))
    n1 = ['杨','孙','利','胡','科']
    n2 = ['余','徐','每','欧','尼','搜']
    n3 = ['风','瑟','墨','句','蓝']
    for i in range(n):
        item = {}
        age = random.randint(18,65)
        id = ids[i]
        name = random.choice(n1)+random.choice(n2)+random.choice(n3)
        item['id'] = id
        item['name'] = name
        item['age'] = age
        data_set.append(item)
    return data_set

data_set = random_list(100)
random.shuffle(data_set)
print(data_set)
print("--------------------")

def person_bubble_sort(li):
    for i in range(len(li)-1):  # 总共遍历len(li)-1次,倒数第二次已得到最终结果
        exchange = False
        for j in range(len(li)-i-1):
            while li[j]['id'] > li[j+1]['id']:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break

    return li

res_li = person_bubble_sort(data_set)
print(res_li)

