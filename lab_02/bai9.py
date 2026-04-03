kw = int(input("Nhap so kw da tieu thu: "))

if kw < 0:
    print("So kw khong hop le")
else:
    if 0 <= kw <= 100:
        don_gia = 2000
    elif 101 <= kw <= 200:
        don_gia = 2500
    elif 201 <= kw <= 300:
        don_gia = 3000
    else: 
        don_gia = 5000

    tien_dien = kw * don_gia
    print("Tien phai tra la: ", tien_dien, "dong")