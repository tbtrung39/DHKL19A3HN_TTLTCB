gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22h): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22h): "))
if 5 <= gio_bat_dau < gio_ket_thuc <= 22:
    thoi_gian_thue = gio_ket_thuc - gio_bat_dau
    gia_goc = 100000
    tong_tien = 0
    if thoi_gian_thue <= 3:
        tong_tien = thoi_gian_thue * gia_goc
    else:
        tong_tien = (3 * gia_goc) + ((thoi_gian_thue - 3) * gia_goc * 0.75)
    if 11 <= gio_bat_dau and gio_ket_thuc <= 15:
        tong_tien = tong_tien * 0.9
    print(f"Tổng tiền thuê sân: {tong_tien:,.0f} đồng")
else:
    print("Giờ thuê không hợp lệ (phải từ 5h đến 22h)!")