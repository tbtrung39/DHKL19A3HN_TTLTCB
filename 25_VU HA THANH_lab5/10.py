def tim_chuoi_chung_dai_nhat(str1, str2):
    n = len(str1)
    for do_dai in range(n, 0, -1):
        for i in range(n - do_dai + 1):
            sub = str1[i : i + do_dai] 
            if sub in str2:
                return sub
    
    return ""

# Nhập dữ liệu
s1 = input("Nhập chuỗi Str1: ")
s2 = input("Nhập chuỗi Str2: ")
ket_qua = tim_chuoi_chung_dai_nhat(s1, s2)

if ket_qua:
    print(f"Chuỗi con chung dài nhất là: '{ket_qua}' (Độ dài: {len(ket_qua)})")
else:
    print("Không có chuỗi con chung.")