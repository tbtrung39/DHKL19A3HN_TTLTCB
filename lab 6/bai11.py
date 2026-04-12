import random
n = int(input("Nhập số phần tử n: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
# a
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(f"Danh sách B: {B}")
# b
C = [x**2 for x in A]
print(f"Danh sách C: {C}")
# c
divisible_by_3 = [x for x in A if x % 3 == 0]
k = min(3, len(divisible_by_3))
D = random.sample(divisible_by_3, k) if divisible_by_3 else []
print(f"Danh sách D (ngẫu nhiên): {D}")