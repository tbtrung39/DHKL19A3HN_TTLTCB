def hoan_vi(danh_sach, l, r, ket_qua):
    if l == r:
        ket_qua.append(danh_sach[:])
    else:
        for i in range(l, r + 1):
            danh_sach[l], danh_sach[i] = danh_sach[i], danh_sach[l]
            hoan_vi(danh_sach, l + 1, r, ket_qua)
            danh_sach[l], danh_sach[i] = danh_sach[i], danh_sach[l]

n = int(input("Nhập n: "))
danh_sach = list(range(1, n + 1))
ket_qua = []

hoan_vi(danh_sach, 0, n - 1, ket_qua)

print(f"Tất cả các hoán vị của [1, 2, ..., {n}]:")
for perm in ket_qua:
    print(perm)
print(f"Tổng cộng {len(ket_qua)} hoán vị")
