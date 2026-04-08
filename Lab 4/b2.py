#a
n = int(input("Nhập số lượng phần tử: "))
i = 1
S = 0
while i <= n:
    if i % 2 == 0:
        S -= 1/i
    else:
        S += 1/i
    i += 1
print("Tổng S =", S)

#b
n = int(input("Nhập số lượng phần tử: "))
i = 2
S = 0
while i <= n + 1:
    S += 1/(i*(i+1))
    i += 1
print("Tổng S =", S)

#c
import math
n = int(input("Nhập số lượng phần tử: "))
i = 2
S = 0
while i <= n + 1:
    S += 1 / math.sqrt(i)
    i += 1
print("Tổng S =", S)

