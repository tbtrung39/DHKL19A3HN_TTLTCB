ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay_trong_thang = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay_trong_thang = 30
elif thang == 2:
    so_ngay_trong_thang = 28
else:
    so_ngay_trong_thang = 0
    
if 1 <= ngay <= so_ngay_trong_thang and so_ngay_trong_thang > 0:
    if ngay == so_ngay_trong_thang:
        if thang == 12:
            ngay_moi = 1
            thang_moi = 1
        else:
            ngay_moi = 1
            thang_moi = thang + 1
    else:
        ngay_moi = ngay + 1
        thang_moi = thang
        
    print("Ngày tiếp theo là: ngày", ngay_moi, "tháng", thang_moi)
else:
    print("Ngày tháng nhập vào không hợp lệ")