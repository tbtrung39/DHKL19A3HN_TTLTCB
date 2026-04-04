a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if a > b:
    x = a
else:
    x = b

if x % a != 0 or x % b != 0:
    x += 1

print("BCNN là: ", x)