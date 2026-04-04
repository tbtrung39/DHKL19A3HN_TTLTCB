str1 = input("Nhập chuỗi thứ nhất (Str1) :")
str2 = input("Nhập chuỗi thứ hai (Str2) :")
i = 0
ket_qua= ""
while i < len(str1) or i < len(str2):
    if i < len(str1):
        ket_qua += str1[i]
    if i < len(str2):
        ket_qua += str2[i]
    i += 1
print("Chuỗi sau khi trộn: ", ket_qua)