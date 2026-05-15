def hoan_vi(ds, trai, phai):
    if trai == phai:
        print(ds)
    else:
        for i in range(trai, phai + 1):
            ds[trai], ds[i] = ds[i], ds[trai]
            hoan_vi(ds, trai + 1, phai)
            ds[trai], ds[i] = ds[i], ds[trai]
n = int(input("Nhap n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i)
hoan_vi(ds, 0, n - 1)