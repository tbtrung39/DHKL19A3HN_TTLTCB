import math

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Sử dụng hàm math.lcm để tìm BCNN
bcnn = math.lcm(a, b)

print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")