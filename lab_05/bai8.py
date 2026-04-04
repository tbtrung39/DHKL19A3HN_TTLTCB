doan_van = input("Nhap doan van ban: ")
tu_don = input("Nhap tu don can tim: ")
dem = 0
tu_hien_tai = ""
doan_van += " "
for ky_tu in doan_van:
    if ky_tu.isspace() == False:
        tu_hien_tai += ky_tu
    else:
        if tu_hien_tai == tu_don:
            dem += 1
        tu_hien_tai = ""
print(f"So lan xuat hien cua tu'{tu_don}' la: {dem}")