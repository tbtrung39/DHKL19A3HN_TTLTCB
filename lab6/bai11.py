n = int(input("Nhap n: "))
A = []
for i in range(n):
    A.append(int(input(f"Nhap phan tu {i+1}: ")))

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B:", B)

C = [x**2 for x in A]
print("C:", C)

import random
D_temp = [x for x in A if x % 3 == 0]
if len(D_temp) > 0:
    D = [random.choice(D_temp)]
    print("D:", D)