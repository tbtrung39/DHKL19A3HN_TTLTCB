#a
def tong(n):
    if n == 1:
        return 1 / (1 * 2)
    return tong(n - 1) + 1 / (n * (n + 1))
n = int(input("Nhap n: "))
print("S =", tong(n))
#b

def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
def tong(n):
    if n == 1:
        return 1
    return tong(n - 1) + 1 / giai_thua(n)
n = int(input("Nhap n: "))
print("S =", tong(n))
#c

import math
def tong(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tong(n - 1))
n = int(input("Nhap n: "))
print("S =", tong(n))
#d
import math
def tong(n):
    if n == 1:
        return math.sqrt(1)
    return (n + tong(n - 1)) ** (1 / (n + 1))
n = int(input("Nhap n: "))
print("S =", tong(n))