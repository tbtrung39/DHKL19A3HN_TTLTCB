def nhap():
    ho_ten = input("Nhap ho ten: ")
    toan = float(input("Nhap diem toan: "))
    ly = float(input("Nhap diem ly: "))
    hoa = float(input("Nhap diem hoa: "))
    return ho_ten, toan, ly, hoa
def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat(ho_ten, dtb):
    print("Ho ten:", ho_ten)
    print("Diem trung binh:", dtb)
ht, t, l, h = nhap()
dtb = tinh_trung_binh(t, l, h)
xuat(ht, dtb)