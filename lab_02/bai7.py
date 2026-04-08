diem = float(input("Nhập điểm tổng kết: "))
if 0.0 <= diem < 3.0:
    print("Loại: Kém")
elif 3.0 <= diem < 5.0: 
    print("Loại: Yếu")
elif 5.0 <= diem < 7.0:
    print("Loại: Trung bình")
elif 7.0 <= diem < 8.0:
    print("Loại: Khá")
elif 8.0 <= diem < 9.0:
    print("Loại: Giỏi")
elif 9.0 <= diem <= 10.0:
    print("Loại: Xuất sắc")
else:
    print("Điểm không hợp lệ!")