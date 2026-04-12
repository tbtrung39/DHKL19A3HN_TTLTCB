import random
A = [] 
for i in range(1000):
    n = random.randint(1, 99999)
    A.append(n)
print(f"Đã sinh xong danh sách gồm {len(A)} số tự nhiên.")