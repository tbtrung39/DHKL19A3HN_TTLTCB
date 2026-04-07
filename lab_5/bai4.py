Str1 = input("Nhập chuỗi 1: ")
Str2 = input("Nhập chuỗi 2: ")
ket_qua = ""
min_len = min(len(Str1), len(Str2))
for i in range(min_len):
    ket_qua += Str1[i] + Str2[i]
ket_qua += Str1[min_len:] + Str2[min_len:]
print(f"Chuỗi sau khi trộn: {ket_qua}")