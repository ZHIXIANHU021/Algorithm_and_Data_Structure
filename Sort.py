import random
import copy
from cal_time import *

@cal_time
def sys_sort(ls):
    ls.sort()
"""
Bubble Sort(O(n^2))
Idea:
Compare two adjacent number and 
swap position if left number great 
than right. repeat steps until all
list has been sorted
"""
def bubble_sort(ls, order='ASC'):
    if order == 'ASC':
        for i in range(len(ls)-1):
            for j in range(len(ls)-i-1):
                if ls[j]>ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
            print(ls)
    else:
        for i in range(len(ls)-1):
            for j in range(len(ls)-i-1):
                if ls[j] < ls[j+1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
            print(ls)

def bubble_sort_v2(ls, order='ASC'):
    """
    Optimal solution added exchange check variable when list
    already be ordered then following steps will be skipped
    """
    if order == 'ASC':
        for i in range(len(ls)-1):
            exchange = False
            for j in range(len(ls)-i-1):
                if ls[j]>ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
                    exchange = True
            print(ls)
            if not exchange:
                return
    else:
        for i in range(len(ls)-1):
            exchange = False
            for j in range(len(ls)-i-1):
                if ls[j] < ls[j+1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
            print(ls)
            if not exchange:
                return

"""
Select Sort(O(n^2))
Cons: High space usage
"""
def select_sort_simple(ls):
    res = []
    for i in range(len(ls)):
        min_val = min(ls)
        res.append(min_val)
        ls.remove(min_val)
    return res

def select_sort(ls):
    for i in range(len(ls)-1):
        min_idx = i
        exchange = False
        for j in range(i+1, len(ls)):
            if ls[j] < ls[min_idx]:
                min_idx = j
                exchange = True
        if min_idx != i:
            ls[i],ls[min_idx] = ls[min_idx], ls[i]
        print(ls)
        if not exchange:
            return

"""
Insert Sort(O(n^2))
"""
# @cal_time
def insert_sort(ls):
    for i in range(1,len(ls)): # i 表示被排序的数字的index
        temp = ls[i]
        j = i-1 # j表示以排序的数字index
        while ls[j] > temp and j >= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = temp
        # print(ls)

# High level Sort methods
"""
Quick Sort(O(nlogn))

Solution idea:
Pick one element p and using element p to make list as two part
elements on the left side of p will smaller than it and elements
on the right side of p will bigger than it. After that using recursion
to finish sort

Cons:
1.Recursion will cost a lots of system sources
and python have recursion limit
2.if list already ordered with reverse side such
as [9,8,7,6,5,4,3,2,1] then partition will happened 
with worst situation with time complexity O(n^2)
"""
def partition(ls,left,right):
    p = ls[left]
    while left < right:
        while ls[right] >= p and left < right:
            right -= 1
        ls[left] = ls[right]
        while ls[left] <= p and left < right:
            left += 1
        ls[right] = ls[left]
    ls[left] = p
    return left

def _quick_sort(ls, left, right):
    if left < right:
        mid = partition(ls,left,right)
        _quick_sort(ls,left,mid-1)
        _quick_sort(ls,mid+1,right)

@cal_time
def quick_sort(ls):
    _quick_sort(ls,0,len(ls)-1)

"""
Quick Sort Optimal version:
Random quick sort
"""

def _random_quick_sort(ls, left, right):
    rand_idx = random.randint(1, len(ls) - 1)
    ls[left], ls[rand_idx] = ls[rand_idx], ls[left]
    if left < right:
        mid = partition(ls, left, right)
        _random_quick_sort(ls, mid+1,  right)
        _random_quick_sort(ls, left, mid-1)

@cal_time
def random_quick_sort(ls):
    _random_quick_sort(ls, 0, len(ls)-1)

"""
Heap Sort(O(nlogn)):
1. Build a heap
2. Found root element that is biggest element
3. Remove root element put last element in the heap to root, then we can implement heap downside adjustment to make new heap
4. Now we have second biggest element on the root
5. Repeat step 3 until we get an empty heap

problem:
top k
"""

def sift(ls, low, high):
    """
    This function for heap adjustment
    :param ls:
    :param low: root node index
    :param high: last element index
    """
    i = low
    j = 2 * i + 1 # j is left child node
    temp = ls[low]
    while j <= high: # 只要j位置有数
        if j + 1 <= high and ls[j+1] > ls[j]: # check if right child node greater than left child node
            j = j + 1 # j指向right child node
        if ls[j] > temp:
            ls[i] = ls[j]
            i = j   # check next level
            j = 2 * i + 1
        else:   # temp 更大，把temp放到i的位置上
            break
    ls[i] = temp

@cal_time
def heap_sort(ls):
    n = len(ls)
    # for loop will create a heap
    for i in range((n-2)//2,-1,-1): # i 表示建堆的时候调整的node index
        sift(ls, i, n-1)

    m = len(ls) - 1
    while m >= 0:
        ls[0], ls[m] = ls[m], ls[0]
        m -= 1
        sift(ls, 0, m)

    # for i in range(n-1,-1,-1):
    #     ls[i], ls[0] = ls[0], ls[i]
    #     sift(ls, 0, i-1)

"""
Top k problem
各项方法时间复杂度对比
1.排序后切片  O(nlogn)
2.LowB三人组 O(kn)
3.堆排序     O(nlogk)

堆排序思路：
1.取列表前k个元素建立一个小根堆
2.依次向后遍历列表，对于列表中的元素，如果小于堆顶，则忽略；如果大于堆顶，则更换为该元素，并对堆进行一次调整
3.遍历列表所以元素后，倒序弹出堆顶
"""
def top_k_1(ls,k):
    sorted(ls)
    return ls[k:]

@cal_time
def top_k_2(ls,k):
    res = ls[:k]
    insert_sort(res)
    for i in range(k,len(ls)):
        if ls[i] > res[0]:
            res[0] = ls[i]
        insert_sort(res)
    return res

def sift_k(ls,low,high): # 调整完后是一个小根堆
    i = low
    j = 2 * i + 1  # j is left child node
    temp = ls[low]
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and ls[j + 1] < ls[j]:  # check if right child node greater than left child node
            j = j + 1  # j指向right child node
        if ls[j] < temp:
            ls[i] = ls[j]
            i = j  # check next level
            j = 2 * i + 1
        else:  # temp 更大，把temp放到i的位置上
            break
    ls[i] = temp

@cal_time
def top_k_3(ls, k):
    heap = ls[:k]
    for i in range((k-2)//2,-1,-1):
        sift_k(heap,i,k-1)

    for i in range(k, len(ls)-1):
        if ls[i] > heap[0]:
            heap[0] = ls[i]
            sift_k(heap,0,k-1)

    for i in range(k-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_k(heap,0,i-1)
    return heap

"""
Merge Sort(O(nlogn))
space complexity(O(n))
"""
def merge(ls,low,mid,high):
    i = low
    j = mid+1
    temp = []
    while i <= mid and j <= high:
        if ls[i] < ls[j]:
            temp.append(ls[i])
            i += 1
        else:
            temp.append(ls[j])
            j += 1
        # 当左右两部分其中一部分没了数的时候结束while loop
    while i <= mid:
        temp.append(ls[i])
        i += 1

    while j <= high:
        temp.append(ls[j])
        j += 1

    ls[low:high+1] = temp
    # print(temp)

def _merge_sort(ls,low,high):
    if low < high: # 至少有两个元素
        mid = (low + high)//2
        _merge_sort(ls,low,mid)
        _merge_sort(ls,mid+1,high)
        merge(ls,low,mid,high)

@cal_time
def merge_sort(ls):
    _merge_sort(ls,0,len(ls)-1)

# Other sort
"""
Shell Sort
1.取一个整数d1 = len(ls)//2,将元素分为d1个组，每组相邻元素之间距离为d1,在各组内进行插入排序
2.取第二个整数d2 = d1//2,重复上述分组排序过程，知道di = 1, 即堆所有元素在同一组内进行直接插入排序

"""
def insert_sort_gap(ls,gap):
    for i in range(gap,len(ls)):
        temp = ls[i]
        j = i - gap
        while j >= 0 and ls[i] > temp:
            ls[j+gap] = ls[j]
            j -= gap
        ls[j+gap] = temp

@cal_time
def shell_sort(ls):
    d = len(ls)//2
    while d >= 1:
        insert_sort_gap(ls,d)
        d //= 2

"""
Count Sort(O(n))
"""
@cal_time
def count_sort(ls,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in ls:
        count[val] += 1
    ls.clear()
    for idx, val in enumerate(count):
        for i in range(val):
            ls.append(idx)

"""
Bucket Sort(O(n+k))
Based on Count Sort
"""
@cal_time
def bucket_sort(ls, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]
    for ele in ls:
        i = min(ele//(max_num//n), n-1)
        buckets[i].append(ele)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_ls = []
    for bin in buckets:
        sorted_ls.extend(bin)
        # sorted_ls += bin
    return sorted_ls

"""
Redix Sort(O(kn))
Based on each digit of number and sort ls
"""
@cal_time
def redix_sort(ls):
    max_num = max(ls)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in ls:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        ls.clear()
        for bucket in buckets:
            ls.extend(bucket)
        it += 1

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(100000)
    # hanoi(7, 'A', 'B', 'C')
    # ls = [random.randint(0,10000) for i in range(10)]
    large_ls = list(range(100000))
    dup_ls = [random.randint(0,100) for _ in range(10000)]
    random.shuffle(large_ls)
    ls = [2,5,3,4,1,6,7,8,9]
    rev_ls = list(range(1000,0,-1))
    large_ls1 = copy.deepcopy(dup_ls)
    large_ls2 = copy.deepcopy(dup_ls)
    large_ls3 = copy.deepcopy(dup_ls)
    # bubble_sort_v2(ls)
    # print(select_sort_simple(ls))
    # print(ls)
    # select_sort(ls)
    # insert_sort(large_ls1)
    # partition(large_ls,1,len(ls)-1)
    quick_sort(large_ls1)
    # random_quick_sort(large_ls2)
    # heap_sort(large_ls2)
    # count_sort(large_ls1,100)
    sys_sort(large_ls2)
    redix_sort(large_ls3)
    # bucket_sort(large_ls3,n=20,max_num=100)
    # shell_sort(large_ls2)
    # merge_sort(large_ls3)
    # print(large_ls1)
    # print(top_k_2(large_ls1,10))
    # print(top_k_3(large_ls2,10))
    # print(ls)
    # print(ls)
    # print(large_ls2)
    # print(ls)
    # 堆排序python内置
    # import heapq #q-> queue 优先队列
    # import random
    # ls = list(range(200))
    # random.shuffle(ls)
    # print(ls)
    # heapq.heapify(ls) # heap build默认小根堆
    # print(ls)
    # for i in range(len(ls)):
    #     print(heapq.heappop(ls), end=',')
