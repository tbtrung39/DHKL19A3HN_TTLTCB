Str = input("Nhập chuỗi: ")
if not Str:
    print("Chuỗi rỗng.")
else:
    max_chuoi = Str[0]
    chuoi_hien_tai = Str[0]
    for i in range(1, len(Str)):
        if Str[i] == Str[i-1]:
            chuoi_hien_tai += Str[i]
        else:
            if len(chuoi_hien_tai) > len(max_chuoi):
                max_chuoi = chuoi_hien_tai
            chuoi_hien_tai = Str[i] 
    if len(chuoi_hien_tai) > len(max_chuoi):
        max_chuoi = chuoi_hien_tai
    print(f"Chuỗi con thỏa mãn: '{max_chuoi}'")