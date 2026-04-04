x = float(input("Nhập giá trị x để tính cos(x): "))
S = 1.0
a = 1.0
n = 1

while a >= 0.0001 or a <= -0.0001:
    a = a * (-1) * x * x / ((2 * n) * (2 * n - 1))
    S = S + a
    n = n + 1

print("Giá trị gần đúng của cos(x) là:", S)