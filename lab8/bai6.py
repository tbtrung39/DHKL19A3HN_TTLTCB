def ucln(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def bcnn(a, b):
    return (a * b) // ucln(abs(a), abs(b))

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

ket_qua = bcnn(a, b)
print(f"BCNN({a}, {b}) = {ket_qua}")
