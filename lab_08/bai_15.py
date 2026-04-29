n = int(input("Nhap so phan tu: "))
ds = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    ds.append(x)
ds_kq = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, ds)))
print("Danh sach ban dau:", ds)
print("Binh phuong cac so le:", ds_kq)