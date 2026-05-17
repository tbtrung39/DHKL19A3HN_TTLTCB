def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

def ucln_n_so(danh_sach, index=0):
    if index == len(danh_sach) - 1:
        return danh_sach[index]
    return ucln(danh_sach[index], ucln_n_so(danh_sach, index + 1))

n = int(input("Nhập số lượng số: "))
danh_sach = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    danh_sach.append(x)

ket_qua = ucln_n_so(danh_sach)
print(f"ƯCLN của {danh_sach} là: {ket_qua}")
