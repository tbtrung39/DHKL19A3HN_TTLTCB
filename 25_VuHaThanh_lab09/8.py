#a
def sum_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return sum_a(n - 1) + 1 / (n * (n + 1))

print("Kết quả câu a (n=3):", sum_a(3)) 
#b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
def sum_b(n):
    if n == 1:
        return 1.0
    return sum_b(n - 1) + 1 / giai_thua(n)
print("Kết quả câu b (n=3):", sum_b(3))
#c
import math

def de_quy_can(i):
    if i == 1:
        return math.sqrt(3)
    return math.sqrt(3 * i + de_quy_can(i - 1))

def sum_c(n):
    if n <= 0:
        return 0
    return de_quy_can(n)

print("Kết quả câu c (n=3):", sum_c(3))