chuoi_nhi_phan = input("Nhap mot chuoi BIN: ")
gia_tri_thap_phan = 0
for ky_tu in chuoi_nhi_phan:
    gia_tri_thap_phan = gia_tri_thap_phan * 2 + int(ky_tu)
print(f"he thap phan tuong ung la: {gia_tri_thap_phan}")
