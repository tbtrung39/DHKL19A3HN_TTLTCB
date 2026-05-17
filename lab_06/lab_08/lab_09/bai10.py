def X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong = tong + (n - i) ** 2 * X(i)
    return tong
n = int(input("Nhap n: "))
print("Xn =", X(n))