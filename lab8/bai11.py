def nhap_sinh_vien():
    ho_ten = input("Nhap ho ten sinh vien: ")
    toan = float(input("Nhap diem Toan: "))
    ly = float(input("Nhap diem Ly: "))
    hoa = float(input("Nhap diem Hoa: "))
    return ho_ten, toan, ly, hoa

def tinh_trung_binh(t, l, h):
    dtb = (t + l + h) / 3
    return dtb

def xuat_ket_qua(ho_ten, dtb):
    print("\n--- Ket qua hoc tap ---")
    print("Sinh vien:", ho_ten)
    print("Diem trung binh: %.2f" % dtb)

ten, d_toan, d_ly, d_hoa = nhap_sinh_vien()
diem_tb = tinh_trung_binh(d_toan, d_ly, d_hoa)
xuat_ket_qua(ten, diem_tb)