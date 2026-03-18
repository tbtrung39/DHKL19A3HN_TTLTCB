diem = float(input("Nhap diem tong ket: "))
if 0 <= diem < 3.0:
    print("Loai kem")
elif 3.0 <= diem < 4.0:
    print("Loai yeu")
elif 4.0 <= diem < 5.0:
    print("Loai trung binh")
elif 5.0 <= diem < 6.0:
    print("Loại trung binh kha")
elif 6.0 <= diem < 7.0:
    print("Loai kha")
elif 7.0 <= diem < 8.0:
    print("Loai Gioi")
elif 8.0 <= diem < 9.0:
    print("Loại Gioi")
elif 9.0 <= diem <= 10:
    print("Loai Xuat sac")
else:
    print("diem khong hop le, nhap lai")