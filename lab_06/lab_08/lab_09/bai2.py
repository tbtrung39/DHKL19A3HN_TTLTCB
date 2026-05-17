def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
n = int(input("Nhap n: "))
x = int(input("Nhap so thu 1: "))
for i in range(2, n + 1):
    y = int(input("Nhap so thu " + str(i) + ": "))
    x = ucln(x, y)
print("UCLN =", x)