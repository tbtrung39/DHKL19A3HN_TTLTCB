n = int(input("Nhập n: "))
ds = [0, 1]
[ds.append(ds[-1] + ds[-2]) for i in range(n - 2)]
print(ds)