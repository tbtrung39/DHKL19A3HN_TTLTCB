st = int(input("Nhập giờ bắt đầu thuê : "))
ed = int(input("Nhập giờ trả sân : "))

times = ed - st
if(st < 5 or ed > 22):
    print("Sân chỉ cho thuê vào 5 giờ sáng và đóng vào lúc 22 giờ tối!")
else:
    if(times <= 0):
        print("Giờ trả sân phải lớn hơn giờ bắt đầu!")
    else:
        gio_giam_gia = max(0, min(ed, 15) - max(st, 11))
        gio_binh_thuong = times - gio_giam_gia
        if times <= 3:
            tong_tien = (gio_binh_thuong * 100000) + (gio_giam_gia * 100000 * 0.9)
        else:
            ty_le_dau = 3 / times
            tien_3h_dau = (gio_binh_thuong * ty_le_dau * 100000) + (gio_giam_gia * ty_le_dau * 100000 * 0.9)
            ty_le_sau = (times - 3) / times
            tien_cac_gio_sau = (gio_binh_thuong * ty_le_sau * 75000) + (gio_giam_gia * ty_le_sau * 75000 * 0.9)
            tong_tien = tien_3h_dau + tien_cac_gio_sau
        print(f"Tổng giờ thuê: {times}h (Trong đó {gio_giam_gia}h được giảm giá)")
        print(f"Tổng tiền: {int(tong_tien)}")