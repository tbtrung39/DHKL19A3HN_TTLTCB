def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", ucln(a, b))