gio = int(input("Nhập số giờ thuê: "))
don_gia = 100000

tien = gio * don_gia

if gio > 3:
    tien *= 0.75   # giảm 25%

print("Tiền thuê sân =", tien)