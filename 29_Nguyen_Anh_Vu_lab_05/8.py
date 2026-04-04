doan_van = input("Nhập đoạn văn bản Str: ")
tu_don = input("Nhập từ đơn cần tìm: ")
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
print(f"Số lần xuất hiện của từ '{tu_don}' là: {dem}")