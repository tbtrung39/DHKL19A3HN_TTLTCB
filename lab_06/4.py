ds = []
while True:
    x = int(input())
    if x == 0:
        break
    ds.append(x)


ds = [1,2,3] + ds + [1,2,3]
if len(ds) >= 5:
    ds[4:4] = [1,2,3]

k = int(input("Nhap k: "))
if 0 <= k < len(ds):
    ds.pop(k)

print(sorted(ds))
print(sorted(ds, reverse=True))