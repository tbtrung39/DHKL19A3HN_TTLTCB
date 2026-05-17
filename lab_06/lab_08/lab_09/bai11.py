def gt_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * gt_kep(n - 2)
k = int(input("Nhap k: "))
tong = 0
for i in range(1, k + 1):
    if i % 2 == 0:
        tong = tong - gt_kep(i)
    else:
        tong = tong + gt_kep(i)
print("S =", tong)