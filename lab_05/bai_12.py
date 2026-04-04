str = input("Nhập chuỗi: ")
tu = ""
for ky_tu in str:
    if ky_tu != " " and ky_tu != ",":
        tu += ky_tu
    else:
        if tu != "":
            print(tu)
            tu = ""
if tu != "":
    print(tu)