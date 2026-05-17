
def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)
n = int(input("n = "))
print("n!! =", giai_thua_kep(n))

k = int(input("k = "))
S = 0
for i in range(1, k + 1):
    S += ((-1) ** (i + 1)) * giai_thua_kep(i)

print("S =", S)