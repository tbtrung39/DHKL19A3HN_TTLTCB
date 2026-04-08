gio_bat_dau = int(input("Nhap gio bat dau: "))
gio_ket_thuc = int(input("Nhap gio ket thuc: "))
so_gio = gio_ket_thuc - gio_bat_dau
if so_gio <= 3:
    tien = so_gio * 100000
else:
    tien = 3 * 100000 + (so_gio - 3) * 75000  
if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
    tien = tien * 0.9
print("Tien phai tra =", tien)