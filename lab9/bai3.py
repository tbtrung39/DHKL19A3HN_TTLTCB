def tinh_luy_thua(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * tinh_luy_thua(a, n - 1)

a = int(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))

ket_qua = tinh_luy_thua(a, n)
print(f"{a}^{n} = {ket_qua}")
