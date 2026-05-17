import random

n = int(input("Nhập số phần tử của danh sách A: "))
A = []
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    A.append(x)

print("Danh sách A:", A)

B = []
for i in range(len(A)):
    if A[i] % 3 == 0 and A[i] % 5 != 0:
        B.append(A[i])
print("Danh sách B (chia hết cho 3 nhưng không chia hết cho 5):", B)

C = []
for i in range(len(A)):
    C.append(A[i] * A[i])
print("Danh sách C (bình phương của A):", C)

D = []
for i in range(len(A)):
    if A[i] % 3 == 0:
        D.append(A[i])
if len(D) > 0:
    random_elements = []
    for i in range(min(3, len(D))):
        random_elements.append(random.choice(D))
    print("Danh sách D (lấy ngẫu nhiên từ A chia hết cho 3):", random_elements)
else:
    print("Danh sách D: Không có phần tử chia hết cho 3")
