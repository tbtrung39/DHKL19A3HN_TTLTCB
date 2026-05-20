def tinh_luy_thua(a, n):
    if n == 0:
        return 1
    
    return a * tinh_luy_thua(a, n - 1)

a = float(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n (số nguyên không âm): "))
if n < 0:
    print("Vui lòng nhập số mũ n >= 0!")
else:
    ket_qua = tinh_luy_thua(a, n)
    print(f"Kết quả của {a}^{n} là: {ket_qua}")