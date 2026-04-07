gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))

thoi_gian_thue = gio_ket_thuc - gio_bat_dau
gia_3_gio_dau = 100000
gia_tiep_theo = gia_3_gio_dau * 0.75  

if thoi_gian_thue <= 3:
    tong_tien = thoi_gian_thue * gia_3_gio_dau
else:
    tong_tien = (3 * gia_3_gio_dau) + ((thoi_gian_thue - 3) * gia_tiep_theo)

if 11 <= gio_bat_dau and gio_ket_thuc <= 15:
    tong_tien = tong_tien * 0.9

print(f"Tổng số tiền thuê sân là: {tong_tien:,.0f} đồng")