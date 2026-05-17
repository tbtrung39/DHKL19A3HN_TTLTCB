n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    ds.append(x)
so_le = list(filter(lambda x: x % 2 != 0, ds))
binh_phuong = list(map(lambda x: x ** 2, so_le))
print("Ket qua:")
print(binh_phuong)