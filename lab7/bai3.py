import random

n = int(input("Nhập n: "))

A = set()
for i in range(n):
    x = random.uniform(0, 100)
    x = round(x, 2)
    A.add(x)

print("Set A (n số thực ngẫu nhiên):", A)
