dtk = float(input("Nhập điểm tổng kết (TK): "))

if 0 <= dtk < 3.0:
    loai = "Kém"
elif 3.0 <= dtk < 4.0:
    loai = "Yếu"
elif 4.0 <= dtk < 6.0:
    loai = "Trung bình"
elif 6.0 <= dtk < 8.0:
    loai = "Khá"
elif 8.0 <= dtk < 9.0:
    loai = "Giỏi"
elif 9.0 <= dtk <= 10.0:
    loai = "Xuất sắc"
else:
    loai = "Điểm không hợp lệ"

print(f"Học lực: {loai}")