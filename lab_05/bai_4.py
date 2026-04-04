str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

res = ""
i = 0

while i < len(str1) or i < len(str2):
    if i < len(str1):
        res += str1[i]
    if i < len(str2):
        res += str2[i]
    i += 1

print("Chuoi sau khi tron:", res)