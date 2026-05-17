from functools import reduce
n = int(input("Nhap n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i)
so_chan = list(filter(lambda x: x % 2 == 0, ds))
tong = reduce(lambda a, b: a + b, so_chan)
print("Tong cac so chan =", tong)