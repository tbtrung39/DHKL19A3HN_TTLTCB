n = int(input("Nhap n: "))
def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)
def tinh_tong_s(k):
    if k == 1:
        return giai_thua_kep(1)
    if (k + 1) % 2 == 0:
        dau = 1
    else:
        dau = -1
    gia_tri_hien_tai = dau * giai_thua_kep(k)
    tong_cac_so_truoc = tinh_tong_s(k - 1)
    return gia_tri_hien_tai + tong_cac_so_truoc
print(f"Ket qua n!!: {giai_thua_kep(n)}")
print(f"Ket qua tong S: {tinh_tong_s(n)}")