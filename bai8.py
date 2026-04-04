s = input("Nhap doan van: ")
tu = input("Nhap tu can tim: ")
dem = 0
word = ""
for i in range(len(s)):
    if s[i] != ' ':
        word = word + s[i]
    else:
        if word == tu:
            dem = dem + 1
        word = ""
if word == tu:
    dem = dem + 1
print("So lan xuat hien:", dem)