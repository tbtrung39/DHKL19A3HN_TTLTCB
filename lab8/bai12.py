def nhap_thong_tin():
    ho_ten = input("Nhap ho ten nhan vien: ")
    que_quan = input("Nhap que quan: ")
    tham_nien = int(input("Nhap tham nien cong tac (nam): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):

    luong = 5000000 + (tham_nien * 500000)
    return luong

def xuat_thong_tin(ho_ten, que_quan, tham_nien, luong):
    print("--- Thong tin nhan vien ---")
    print("Ho ten:", ho_ten)
    print("Que quan:", que_quan)
    print("Tham nien:", tham_nien, "nam")
    print("Luong: ", luong, "VND")

ten, que, nam, tien_luong = 0, 0, 0, 0
ten, que, nam = nhap_thong_tin()
tien_luong = tinh_luong(nam)
xuat_thong_tin(ten, que, nam, tien_luong)