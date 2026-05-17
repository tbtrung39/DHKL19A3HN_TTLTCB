def ucln(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

ket_qua = ucln(abs(a), abs(b))
print(f"ƯCLN({a}, {b}) = {ket_qua}")
