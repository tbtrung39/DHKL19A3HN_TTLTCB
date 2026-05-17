def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)
a = int(input("Nhập a: "))
n = int(input("Nhập n: "))
print("Kết quả =", power(a, n))