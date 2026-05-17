import random
n = int(input("Nhap n: "))
A = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    A.append(x)
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sach B:", B)
C = [x**2 for x in A]
print("Danh sach C:", C)
D = random.sample([x for x in A if x % 3 == 0],
                  len([x for x in A if x % 3 == 0]))

print("Danh sach D:", D)