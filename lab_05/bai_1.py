chuoi = input("Nhập chuỗi: ")
dem = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():  # kiểm tra có phải là số không
        dem += 1
print("Số ký tự là số trong chuỗi:", dem)