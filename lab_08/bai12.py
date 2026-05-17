def nhap_thong_tin_nhan_vien():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quế quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    if tham_nien < 1:
        luong = luong_co_ban
    elif tham_nien < 3:
        luong = luong_co_ban * 1.1
    elif tham_nien < 5:
        luong = luong_co_ban * 1.15
    else:
        luong = luong_co_ban * 1.2
    return luong

def xuat_thong_tin_nhan_vien(ho_ten, que_quan, tham_nien, luong):
    print("=== Thông tin nhân viên ===")
    print(f"Họ tên: {ho_ten}")
    print(f"Quế quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong:,.0f} VND")

ho_ten, que_quan, tham_nien = nhap_thong_tin_nhan_vien()
luong = tinh_luong(tham_nien)
xuat_thong_tin_nhan_vien(ho_ten, que_quan, tham_nien, luong)
