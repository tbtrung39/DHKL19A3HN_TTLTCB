gio_thue = int(input("Nhap so gio thue san: "))

if gio_thue <= 0:
    print("Thoi gian thue khong hop le")
else:
    if gio_thue <= 3:
        tien = gio_thue * 100000
    else:
        tien = 3 * 100000 + (gio_thue - 3) * (100000 * 0.75)

    bat_dau = int(input("Nhap so gio bat dau (6-21): "))
    if 11 <= bat_dau <= 15:
        tien = tien * 0.8

    print("tien thue san la:", tien, "dong")