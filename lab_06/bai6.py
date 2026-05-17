import random
A = []
for i in range(1000):
    A.append(random.randint(1, 99999))
print("danh sach ban dau")
print(A)
B = sorted(A)
print("tang dan ")
print(B)