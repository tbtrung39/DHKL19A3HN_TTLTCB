Str = input("Nhập chuỗi: ")
Str_xu_ly = Str.replace(',', ' ')
cac_tu = Str_xu_ly.split()
print("Các từ trong chuỗi:")
for tu in cac_tu:
    print(tu)