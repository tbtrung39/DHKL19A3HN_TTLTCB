bat_dau = int(input("Nhap gio bat dau (6-21): "))
ket_thuc = int(input("Nhap gio ket thuc (7-22): "))

if bat_dau < 6 or ket_thuc > 22 or bat_dau >= ket_thuc:
    print("Gio nhap khong hop le")
else:
    gio_thue = ket_thuc - bat_dau
    if gio_thue <= 3:
        tien = gio_thue * 100000
    else:
        tien = 3 * 100000 + (gio_thue - 3) * (100000 * 0.75)

    if 11 <= bat_dau <= 15:
        tien = tien * 0.8

    print("Tien thue san la:", tien, "đong")