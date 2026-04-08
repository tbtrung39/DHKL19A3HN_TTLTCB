Str1 = input("Nhập chuỗi thứ nhất (Str1): ")
Str2 = input("Nhập chuỗi thứ hai (Str2): ")
Str_ket_qua = ""
i = 0
while i < len(Str1) or i < len(Str2):
    if i < len(Str1): 
        Str_ket_qua = Str_ket_qua + Str1[i] 
    if i < len(Str2): 
        Str_ket_qua = Str_ket_qua + Str2[i] 
    i = i + 1

print("Chuỗi sau khi trộn là:", Str_ket_qua)