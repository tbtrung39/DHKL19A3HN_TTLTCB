Str = input("Nhập chuỗi: ")
tu = input("Nhập từ cần tìm: ")
ds = Str.split()
dem = 0
i = 0
while i < len(ds):
    if ds[i] == tu:
        dem += 1
    i += 1
print("Số lần xuất hiện:", dem)