# Bước 1: Nhập chuỗi
s = input("Nhập vào chuỗi Str: ")

chuoi_con_dai_nhat = ""
chuoi_tam_thoi = ""

for i in range(len(s)):
    if i == 0 or s[i] == s[i-1]:
        chuoi_tam_thoi += s[i]
    else:
        chuoi_tam_thoi = s[i]
    
    if len(chuoi_tam_thoi) > len(chuoi_con_dai_nhat):
        chuoi_con_dai_nhat = chuoi_tam_thoi

print("Chuỗi con dài nhất gồm các ký tự giống nhau là:", chuoi_con_dai_nhat)