#a

def S(n):
    if n == 1:
        return 1 / (1 * 2)
    return S(n - 1) + 1 / (n * (n + 1))
n = int(input("n = "))
print(S(n))

#b


def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)


def S(n):
    if n == 1:
        return 1
    return S(n - 1) + 1 / giai_thua(n)
n = int(input("n = "))
print(S(n))

#c

import math
def tinh_S(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_S(n - 1))
n = int(input("Nhập n: "))
print("S =", tinh_S(n))

#d

def tinh(n):
    if n == 1:
        return (1 + 1 ** 0.5) ** (1 / 2)
    return (n + tinh(n - 1)) ** (1 / (n + 1))
n = int(input("Nhập n: "))
s = tinh(n)
print("S =", s)

