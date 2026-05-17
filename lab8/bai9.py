def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Lỗi: không chia được cho 0"

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

print(f"{a} + {b} = {cong(a, b)}")
print(f"{a} - {b} = {tru(a, b)}")
print(f"{a} * {b} = {nhan(a, b)}")
print(f"{a} / {b} = {chia(a, b)}")
