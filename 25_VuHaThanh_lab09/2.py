#1
def ucln_2_so(a, b):
    if b == 0:
        return a
    return ucln_2_so(b, a % b)
#2
def ucln_n_so(danh_sach):
    if len(danh_sach) == 1:
        return danh_sach[0]
    return ucln_2_so(danh_sach[0], ucln_n_so(danh_sach[1:]))

n = int(input("Nhập số lượng số n = "))
cac_so = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i+1}: "))
    cac_so.append(so)

ket_qua = ucln_n_so(cac_so)
print(f"Ước chung lớn nhất của {n} số vừa nhập là: {ket_qua}")