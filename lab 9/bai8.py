# a
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S += 1 / (i * (i + 1))
print("S =", S)

# b
n = int(input("Nhập n: "))
S = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    S += 1 / fact
print("S =", S)

# c
import math
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S = math.sqrt(3 * i + S)
print("S =", S)

# d
def tinh_S(i, n):
    if i == 1:
        return 1 ** (1/2)
    return (i + tinh_S(i - 1, n)) ** (1 / (i + 1))
n = int(input("Nhập n: "))
S = tinh_S(n, n)
print("S =", S)