from functools import reduce
n = int(input("Nhap so phan tu: "))
ds = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    ds.append(x)
ds_chan = list(filter(lambda x: x % 2 == 0, ds))
# tinh tong bang reduce
tong = reduce(lambda a, b: a + b, ds_chan, 0)
print("Danh sach ban dau:", ds)
print("Cac so chan:", ds_chan)
print("Tong cac so chan:", tong)