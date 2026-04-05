Str = input("Nhập vào một chuỗi ký tự: ")
dem = 0
for c in Str:
    if c.isdigit():
        dem += 1
print(f"Số lượng ký tự là số trong chuỗi: {dem}")