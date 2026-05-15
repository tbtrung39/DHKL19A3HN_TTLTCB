import random
n = int(input("Nhap n: "))
A = []
for i in range(1, n + 1):
    A.append(i)
result = []
while len(A) > 0:
    vi_tri = random.randint(0, len(A) - 1)
    result.append(A[vi_tri])
    A.pop(vi_tri)
print("Hoan vi ngau nhien:")
print(result)

