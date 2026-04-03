n = int(input("nhap gio bat dau : "))
t = int(input("nhap gio ket thuc: "))
if n <= 5 or t > 22 or n >= t:
    print("khong hop le")
else:
    so_gio = t - n
    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3 * 100000 + (so_gio - 3) * (100000 * 0.75)
    if n >= 11 and t <= 15:
        tien = (so_gio * 100000) * 0.9
    print("so tien phai tra là: ",tien,"dong") 