tntc = int(input("Nhap TNTC của nhân viên:"))
can_ban = 1350000
if tntc < 12:
    luong = 2.34*can_ban
    print("lương của nhân viên là:",luong,"đồng")
elif 12 <= tntc < 36:
    luong = 3.33*can_ban
    print("lương của nhân viên là:",luong,"đồng")
elif 36 <= tntc < 60:
    luong = 3.66*can_ban
    print("lương của nhân viên là:",luong,"đồng")
else:
    luong = 3.99*can_ban
    print("lương của nhân viên là:",luong,"đồng")