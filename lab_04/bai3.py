import math
x = float(input("Nhập x (radian): "))
sai_so = 0.0001
cos_x = 1.0
term = 1.0
n = 1
while True:
    term *= -x**2 / ((2*n) * (2*n - 1))
    if abs(term) < sai_so:
        break
    cos_x += term
    n += 1
print(f"Giá trị gần đúng của cos({x}) là: {cos_x:.4f}")
print(f"Giá trị thực tế: {math.cos(x):.4f}")