from cal_time import *

def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    return fibnacci(n-1) + fibnacci(n-2)

"""
Dynamic Programming = 递推式 + 重复子问题
"""

def fibnacci_no_recursion(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[-1]

"""
钢条切割问题”
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
求切割钢条方案，使得收益最大化
"""
def cut_rod_recursion(p, n):
    if n == 0:
        return 0
    res = p[n]
    for i in range(1, n):
        res = max(res, cut_rod_recursion(p, i) + cut_rod_recursion(p, n-i))
    return res

def cut_rod_dp(p, n):
    if n == 0:
        return 0
    res = 0
    for i in range(1, n+1):
        res = max(res, p[i] + cut_rod_dp(p, n-i))
    return res

@cal_time
def cut_rod1(p, n):
    return cut_rod_recursion(p, n)

@cal_time
def cut_rod2(p, n):
    return cut_rod_dp(p, n)

@cal_time
def cut_rod_dp2(p, n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j] + r[i-j])
        r.append(res)
    return r[n]

def cut_rod_return_cut(p, n):
    r = [0]
    s = [0]
    for i in range(1, n+1):
        res = 0
        res_s = 0
        for j in range(1, i+1):
            if p[j] + r[i - j] > res:
                res = p[j] + r[i - j]
                res_s = j
        r.append(res)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n):
    r, s = cut_rod_return_cut(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return r, ans

"""
最长公共子序列
X = 'ABBCCBDE'
Y = 'DBBCDB'
LCS(X, Y) = 'BBCD'
"""
def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]: # i, j位置上的字符匹配的时候，来自与左上方+1
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]

def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # 1 左上 2 上方 3 左方
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]: # i, j位置上的字符匹配的时候，来自与左上方+1
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '↖'
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '←'
    return c[m][n], b

def lcs_traceback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == '↖':
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == '↑':
            i -= 1
        else:
            j -= 1

    return ''.join(res[::-1])


"""
最大公约数 -- 欧几里得算法
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd2(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x


    def gcd(self, a, b):
        while b > 0:
            c = a % b
            a = b
            b = c
        return a

    def lcm(self, a, b):
        x = gcd(a, b)
        return (a * b) / x

    def __add__(self, other):
        # 1/12 + 1/20
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        deno = self.lcm(b, d)
        mole = a * (deno / b) + c * (deno / d)
        return Fraction(mole, deno)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

if __name__ == '__main__':
    # print(fibnacci(10))
    # print(fibnacci_no_recursion(100))
    # p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
    # print(cut_rod_recursion(p, 20))
    # print(cut_rod_dp(p, 20))
    # # print(cut_rod1(p, 15))
    # print(cut_rod2(p, 20))
    # print(cut_rod_dp2(p, 20))
    # print(cut_rod_return_cut(p, 20))
    # print(cut_rod_solution(p, 20))
    # X = 'ABBCCBDE'
    # Y = 'DBBCDB'
    # print(lcs_length(X, Y))
    # print(lcs_traceback(X, Y))
    # print(gcd(12, 16))
    # print(gcd2(12, 16))
    # f = Fraction(12, 16)
    # print(f)
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    print(a + b)