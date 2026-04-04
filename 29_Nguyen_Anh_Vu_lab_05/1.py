chuoi = input("Nhập chuỗi Str: ")
dem = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        dem += 1
print(f"Số lượng ký tự là số trong chuỗi: {dem}")