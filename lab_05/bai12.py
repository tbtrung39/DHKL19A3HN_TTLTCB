str1 = "Khoa, khoa hoc ung dung"
chuoi_da_don_dep = str1.replace(",", " ") 
danh_sach_cac_tu = chuoi_da_don_dep.split() 
for tu in danh_sach_cac_tu:
    print(tu) 