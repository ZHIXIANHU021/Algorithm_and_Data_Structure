from functools import cmp_to_key
t = [100, 50, 20, 5, 1]
def change(t, n):
    """
    找零问题
    """
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n %= money
    return m, n

def fraction_backpack(goods, w):
    goods.sort(key=lambda x:x[0]/x[1], reverse=True)
    res = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            res[i] = 1
            w -= weight
            total_v += prize
        else:
            res[i] = w/weight
            total_v += res[i] * prize
            break
    return total_v, res

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(ls):
    """
    拼数问题：
    把list里的数按照string相加的方式合并然后返回可以组成的最大数
    """
    ls = list(map(str, ls))
    ls.sort(key=cmp_to_key(xy_cmp))
    return "".join(ls)

def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
       if a[i][0] >= res[-1][1]:
           res.append(a[i])
    return res

if __name__ == "__main__":
    goods = [(60, 10), (100, 20), (120, 30)] # 每个商品元组表示（价格，重量）
    ls = [32, 94, 128, 1286, 6, 71]
    activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    activities.sort(key=lambda x:x[1])
    # print(change(t, 1001))
    # print(fraction_backpack(goods, 50))
    # print(number_join(ls))
    print(activity_selection(activities))