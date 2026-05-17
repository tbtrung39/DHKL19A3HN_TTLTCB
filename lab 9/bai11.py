def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)
def tinh_S(k):
    tong = 0
    for i in range(1, k + 1):
        if i % 2 == 1:
            tong += double_factorial(i)
        else:
            tong -= double_factorial(i)
    return tong
k = int(input("Nhập k: "))
print("S =", tinh_S(k))