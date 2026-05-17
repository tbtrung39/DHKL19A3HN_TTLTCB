def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
    return trung_binh

ho_ten = input("Nhập họ tên: ")
diem_toan = float(input("Nhập điểm Toán: "))
diem_ly = float(input("Nhập điểm Lý: "))
diem_hoa = float(input("Nhập điểm Hóa: "))

diem_trung_binh = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)

print(f"Họ tên: {ho_ten}")
print(f"Điểm Toán: {diem_toan}")
print(f"Điểm Lý: {diem_ly}")
print(f"Điểm Hóa: {diem_hoa}")
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
