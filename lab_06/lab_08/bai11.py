def sinh_vien():
    ten = input("Nhap ho ten: ")
    toan = float(input("Nhap diem Toan: "))
    ly = float(input("Nhap diem Ly: "))
    hoa = float(input("Nhap diem Hoa: "))
    dtb = (toan + ly + hoa) / 3
    print("Ho ten:", ten)
    print("Diem trung binh:", dtb)
sinh_vien()