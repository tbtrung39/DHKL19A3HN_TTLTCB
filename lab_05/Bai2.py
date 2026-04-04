Str = input("Nhập chuỗi Str: ")
dem = 0
for c in Str:
    if not c.isalnum():  # Hàm kiểm tra có phải là chữ cái hoặc số hay không
        dem += 1
print("Số ký tự không phải chữ và số:", dem)