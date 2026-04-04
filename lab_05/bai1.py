Str = input("Nhập chuỗi Str: ")
dem = 0
for c in Str:
    if c.isdigit():  # Hàm kiểm tra ký tự số
        dem += 1
print("Số các ký tự là số:", dem)