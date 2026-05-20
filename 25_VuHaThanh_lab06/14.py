chuoi_nhap = input("Nhập vào các mật khẩu (cách nhau bởi dấu phẩy): ")
danh_sach_mat_khau = chuoi_nhap.split(',')
mat_khau_hop_le = []
ky_tu_dac_biet = ["$", "#", "@"]
for mk in danh_sach_mat_khau:
    mk = mk.strip()
    if len(mk) < 6 or len(mk) > 12:
        continue
        
    co_chu_thuong = False 
    co_so = False         
    co_chu_hoa = False   
    co_ky_tu_db = False    
    
    for ky_tu in mk:
        if ky_tu.islower():   
            co_chu_thuong = True
        elif ky_tu.isdigit(): 
            co_so = True
        elif ky_tu.isupper(): 
            co_chu_hoa = True
        elif ky_tu in ky_tu_dac_biet: 
            co_ky_tu_db = True

    if co_chu_thuong and co_so and co_chu_hoa and co_ky_tu_db:
        mat_khau_hop_le.append(mk) 
print(",".join(mat_khau_hop_le))