ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay_max = 31
elif thang in [4, 6, 9, 11]:
    so_ngay_max = 30
elif thang == 2:
    so_ngay_max = 28
else:
    so_ngay_max = 0
if 1 <= ngay <= so_ngay_max and 1 <= thang <= 12:
    if ngay < so_ngay_max:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        nam_tiep_theo = nam
    else: 
        ngay_tiep_theo = 1
        if thang < 12:
            thang_tiep_theo = thang + 1
            nam_tiep_theo = nam
        else: 
            thang_tiep_theo = 1
            nam_tiep_theo = nam + 1
    print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}/{nam_tiep_theo}")
else:
    print("Ngày hoặc tháng nhập vào không hợp lệ!")