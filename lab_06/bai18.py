m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))
A = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        hang.append(x)
    A.append(hang)
print("Ma tran A:")
for i in A:
    print(i)
tong = 0
for i in A:
    tong += sum(i)
print("Tong cac phan tu:", tong)