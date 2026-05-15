def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
def ucln_day(ds, n):
    if n == 1:
        return ds[0]
    else:
        return ucln(ds[n - 1], ucln_day(ds, n - 1))
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input("Nhap so: "))
    ds.append(x)
print("UCLN cua day la:", ucln_day(ds, n))