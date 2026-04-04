s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
max_chuoi = ""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        chuoi_con = s1[i:j]
        if chuoi_con in s2:
            if len(chuoi_con) > len(max_chuoi):
                max_chuoi = chuoi_con
print("Chuỗi chung dài nhất:", max_chuoi)