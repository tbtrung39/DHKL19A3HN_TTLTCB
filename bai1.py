s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if '0' <= c <= '9':
        dem = dem + 1
print("Số kí tự là số:", dem)