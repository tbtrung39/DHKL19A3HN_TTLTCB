import random
n = int(input("Nhap so luong phan tu: "))
A = []

for i in range(n):
    so = int(input("Nhap so: "))
    A.append(so)
# a)
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sach B:", B)
# b)
C = [x**2 for x in A]
print("Danh sach C:", C)
# c)
D = [x for x in A if x % 3 == 0]
print("Danh sach D:", D)