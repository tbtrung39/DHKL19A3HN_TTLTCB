import re

str1 = input("Nhập chuỗi Str1: ")
danh_sach_tu = re.split(r'[ ,]+', str1)
for tu in danh_sach_tu:
    if tu: 
        print(tu)