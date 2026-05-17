import random
def tron(ds):
    if len(ds) == 0:
        return []
    x = random.choice(ds)
    ds.remove(x)
    return [x] + tron(ds)
n = int(input("Nhap n: "))
a = []
for i in range(1, n + 1):
    a.append(i)
print(tron(a))