m = int(input("Nhap so hang m: "))
n = int(input("Nhap so cot n: "))

A = []
for i in range(m):
    hang = []
    for j in range(n):
        so = int(input(f"Nhap phan tu A[{i}][{j}]: "))
        hang.append(so)
    A.append(hang)

tong = 0
for hang in A:
    for phan_tu in hang:
        tong = tong + phan_tu

print("Ma tran A:")
for hang in A:
    print(hang)
print("Tong cac phan tu:", tong)