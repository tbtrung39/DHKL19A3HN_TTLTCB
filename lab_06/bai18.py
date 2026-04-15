m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        so = int(input(f"Nhap phan tu [{i}][{j}]: "))
        hang.append(so)
    ma_tran.append(hang)
tong = 0
for i in range(m):
    for j in range(n):
        tong = tong + ma_tran[i][j]
print("Tong cac phan tu:", tong)