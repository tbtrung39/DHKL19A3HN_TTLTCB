tnct = int(input("Nhap thoi gian cong tac: "))
luong_can_ban = 1350000

if tnct < 0:
    print("Thoi gian cong tac khong hop le")
else:
    if tnct < 12:
        he_so = 2.34
    elif 12 <= tnct < 36:
        he_so = 3.33
    elif 36 <= tnct < 60:
        he_so = 3.66
    else: 
        he_so = 3.9

    luong = he_so * luong_can_ban
    print("Luong nhan vien la:", luong, "dong")