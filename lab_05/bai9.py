s = input("Nhập chuỗi: ")
max_chuoi = ""
chuoi_hien_tai = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        chuoi_hien_tai += s[i]
    else:
        if len(chuoi_hien_tai) > len(max_chuoi):
            max_chuoi = chuoi_hien_tai
        chuoi_hien_tai = s[i]
if len(chuoi_hien_tai) > len(max_chuoi):
    max_chuoi = chuoi_hien_tai
print("Chuỗi con dài nhất:", max_chuoi)