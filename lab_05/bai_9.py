str = input("Nhập chuỗi: ")
chuoi_max = ""
chuoi_hien_tai = str[0]
for i in range(1, len(str)):
    if str[i] == str[i-1]:
        chuoi_hien_tai += str[i]
    else:
        if len(chuoi_hien_tai) > len(chuoi_max):
            chuoi_max = chuoi_hien_tai
        chuoi_hien_tai = str[i]
if len(chuoi_hien_tai) > len(chuoi_max):
    chuoi_max = chuoi_hien_tai
print("Chuỗi con dài nhất:", chuoi_max)