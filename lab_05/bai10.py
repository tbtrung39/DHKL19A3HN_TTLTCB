str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")
chuoi_chung_max = ""
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2:
            if len(chuoi_con) > len(chuoi_chung_max):
                chuoi_chung_max = chuoi_con
print("Chuoi con chung dai nhat la:", chuoi_chung_max)