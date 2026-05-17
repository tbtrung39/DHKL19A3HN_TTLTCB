def permutation(ds, l, r):
    if l == r:
        print(ds)
    else:
        for i in range(l, r + 1):
            ds[l], ds[i] = ds[i], ds[l]
            permutation(ds, l + 1, r)
            ds[l], ds[i] = ds[i], ds[l]
n = int(input("Nhap n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i)
permutation(ds, 0, n - 1)