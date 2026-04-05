bat_dau = int(input("nhập giờ bắt đầu: "))
ket_thuc = int(input("nhập giờ kết thúc: "))
if bat_dau <= 5 or ket_thuc > 22 or bat_dau >= ket_thuc:
    print("không hợp lệ!")
else:
    print("tính tiền")