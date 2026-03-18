'''10. Một điểm cho thuê sân tập bóng đá theo công thức sau:
- Mỗi giờ trong 3 giờ đầu tiên tính 100.000 đồng/giờ
- Mỗi giờ tiếp theo có đơn giá giảm 25% so với đơn giá trong 3 giờ đầu tiên
- Ngoài ra nếu thời gian thuê sân từ 11 giờ đến 15 giờ thì được giảm giá thêm 10%'''

bat_dau = int(input("Nhập giờ bắt đầu: "))
ket_thuc = int(input("Nhập giờ kết thúc: "))

so_gio = ket_thuc - bat_dau
don_gia = 100000

if so_gio <= 3:
    tien = so_gio * don_gia
else:
    tien = 3 * don_gia + (so_gio - 3) * (don_gia * 0.75)

if 11 <= bat_dau < 15 or 11 < ket_thuc <= 15 or (bat_dau <= 11 and ket_thuc >= 15):
    tien *= 0.9

print("Số giờ thuê:", so_gio)
print("Số tiền phải trả:", tien, "đồng")