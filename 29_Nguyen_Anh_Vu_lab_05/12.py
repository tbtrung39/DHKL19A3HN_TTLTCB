chuoi_nhap = input("Nhập chuỗi Str1: ")
print("Các từ trong chuỗi là:")
tu_hien_tai = ""
chuoi_nhap += " "
for ky_tu in chuoi_nhap:
    if ky_tu.isspace() or ky_tu == ",":
        if tu_hien_tai != "":
            print(tu_hien_tai)
            tu_hien_tai = ""
    else:
        tu_hien_tai += ky_tu