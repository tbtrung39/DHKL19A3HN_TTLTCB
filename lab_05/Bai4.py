Str1=input("Nhập chuỗi 1: ")
Str2=input("Nhập chuỗi 2: ")

i = 0
kq = ""
while i < len(Str1) or i < len(Str2):
    if i < len(Str1):
        kq += Str1[i]
    if i < len(Str2):
        kq += Str2[i]
    i += 1
print("Chuỗi sau khi trộn: ", kq)

