n = int(input("Nhập n: "))
s = 0
for i in range(1, n + 1):
    if i % 2 == 1: # Nếu là số lẻ thì cộng
        s += 1/i
    else:          # Nếu là số chẵn thì trừ
        s -= 1/i
print("Tổng S2a =", s)

n = int(input("Nhập n: "))
s = 0
for i in range(1, n + 1):
    s += 1 / (i * (i + 1))
print("Tổng S2b =", s)

import math # Cần thư viện math để dùng căn bậc hai

n = int(input("Nhập n: "))
s = 0
for i in range(2, n + 2): # Chạy từ 2 đến n+1
    s += 1 / math.sqrt(i)
print("Tổng S2c =", s)