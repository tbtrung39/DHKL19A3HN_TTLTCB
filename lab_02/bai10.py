bat_dau = int(input("nhap gio bat dau: "))
ket_thuc = int(input("nhap gio ket thuc: "))
so_gio = bat_dau - ket_thuc
if so_gio <= 3:
    tien = so_gio * 100000
else:
    tien = 3 * 100000 + (so_gio - 3) * (100000 * 0.75)
if bat_dau >= 11 and ket_thuc <= 15:
    tien = (so_gio * 100000) * 0.9
print("so tien phai tra là: ",tien,"dong")