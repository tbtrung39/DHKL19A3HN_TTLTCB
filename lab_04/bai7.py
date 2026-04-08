a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
x, y = a, b
while y:
    x, y = y, x % y
ucln = x
bcnn = abs(a * b) // ucln
print(f"BCNN của {a} và {b} là: {bcnn}")