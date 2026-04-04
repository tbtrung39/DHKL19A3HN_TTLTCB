chuoi_nhi_phan = input("Nhập một chuỗi BIN: ")
gia_tri_thap_phan = 0
for ky_tu in chuoi_nhi_phan:
    gia_tri_thap_phan = gia_tri_thap_phan * 2 + int(ky_tu)
print(f"Hệ thập phân tương ứng là: {gia_tri_thap_phan}")