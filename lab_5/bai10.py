Str1 = input("Nhập chuỗi 1: ")
Str2 = input("Nhập chuỗi 2: ")
max_len = 0
chuoi_con_chung = ""
for i in range(len(Str1)):
    for j in range(len(Str2)):
        k = 0
        while (i + k < len(Str1)) and (j + k < len(Str2)) and (Str1[i+k] == Str2[j+k]):
            k += 1
        if k > max_len:
            max_len = k
            chuoi_con_chung = Str1[i:i+k]
if max_len > 0:
    print(f"Chuỗi con chung dài nhất: '{chuoi_con_chung}' (độ dài {max_len})")
else:
    print("Không có chuỗi con chung.")