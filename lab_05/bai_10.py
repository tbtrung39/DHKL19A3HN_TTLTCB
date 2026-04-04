str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")
max_str = ""
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        if sub in str2 and len(sub) > len(max_str):
            max_str = sub
print("Chuoi con chung dai nhat:", max_str)