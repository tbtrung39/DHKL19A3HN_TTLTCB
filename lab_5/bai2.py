Str = input("Nhập vào một chuỗi ký tự: ")
dem = 0
for c in Str:
    if not c.isalnum():
        dem += 1
print(f"Số lượng ký tự không phải chữ và số: {dem}")