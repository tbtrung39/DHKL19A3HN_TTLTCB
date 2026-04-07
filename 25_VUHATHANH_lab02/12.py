ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Danh sách số ngày của từng tháng (năm không nhuận)
ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Tăng thêm 1 ngày
ngay += 1

# Kiểm tra nếu vượt quá số ngày trong tháng
if ngay > ngay_trong_thang[thang]:
    ngay = 1
    thang += 1
    
    # Kiểm tra nếu vượt quá tháng 12
    if thang > 12:
        thang = 1
        nam += 1

print(f"Ngày tiếp theo là: {ngay}/{thang}/{nam}")