def nhap():
    ho_ten = input("Nhap ho ten: ")
    que_quan = input("Nhap que quan: ")
    tham_nien = int(input("Nhap tham nien cong tac (nam): "))
    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 3000000
    he_so = 1 + tham_nien * 0.1
    return luong_co_ban * he_so
def xuat(ho_ten, que_quan, tham_nien, luong):
    print("Ho ten:", ho_ten)
    print("Que quan:", que_quan)
    print("Tham nien:", tham_nien)
    print("Luong:", luong)
ht, qq, tn = nhap()
luong = tinh_luong(tn)
xuat(ht, qq, tn, luong)