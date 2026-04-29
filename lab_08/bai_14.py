# nhap list
n = int(input("Nhap so phan tu: "))
ds = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    ds.append(x)
ds_binh_phuong = list(map(lambda x: x**2, ds))
print("Danh sach ban dau:", ds)
print("Danh sach binh phuong:", ds_binh_phuong)