chuoi_nhap = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")
danh_sach_matkhau = chuoi_nhap.split(",")
matkhau_hoiple = []

for matkhau in danh_sach_matkhau:
    matkhau = matkhau.strip()
    co_thuong   = False
    co_hoa      = False
    co_so       = False
    co_dacbiet  = False

    for ky_tu in matkhau:
        if ky_tu in "abcdefghijklmnopqrstuvwxyz": co_thuong  = True
        if ky_tu in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": co_hoa     = True
        if ky_tu in "0123456789":                 co_so      = True
        if ky_tu in "$#@":                        co_dacbiet = True

    if co_thuong and co_hoa and co_so and co_dacbiet and 6 <= len(matkhau) <= 12:
        matkhau_hoiple.append(matkhau)

print(", ".join(matkhau_hoiple))