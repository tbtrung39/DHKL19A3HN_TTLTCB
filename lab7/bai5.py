import random
danh_sach_goc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A = set()
while len(A) < 5:
    A.add(random.choice(danh_sach_goc))
print(A)