str = input("Nhap doan van: ")
tu = input("Nhap tu can tim: ")
ds = str.split()
dem = 0
for i in ds:
    if i == tu:
        dem = dem + 1
print("So lan xuat hien:", dem)