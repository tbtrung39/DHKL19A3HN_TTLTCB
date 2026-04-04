diem = float(input("Nhập điểm tổng kết của học sinh: "))

if 0.0 <= diem < 3.0:
    print("Học lực: Loại Kém")
elif 3.0 <= diem < 5.0:
    print("Học lực: Loại Yếu")
elif 5.0 <= diem < 7.0:
    print("Học lực: Loại Trung bình")
elif 7.0 <= diem < 8.0:
    print("Học lực: Loại Khá")
elif 8.0 <= diem < 9.0:
    print("Học lực: Loại Giỏi")
elif 9.0 <= diem <= 10.0:
    print("Học lực: Loại Xuất sắc")
else:
    print("Điểm nhập vào không hợp lệ")