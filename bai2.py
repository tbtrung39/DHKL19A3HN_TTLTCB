s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if not(('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
        dem = dem + 1
print("Số kí tự đặc biệt:", dem)


