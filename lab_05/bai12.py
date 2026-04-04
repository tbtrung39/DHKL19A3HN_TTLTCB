s = input("Nhập chuỗi: ")
tu = ""
for c in s:
    if c != ' ' and c != ',':
        tu += c
    else:
        if tu != "":
            print(tu)
            tu = ""
if tu != "":
    print(tu)