def mu(a, n):
    if n == 0:
        return 1
    return a * mu(a, n - 1)
a = int(input("Nhap a: "))
n = int(input("Nhap n: "))
print("Ket qua =", mu(a, n))