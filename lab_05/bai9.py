chuoi_nhap = input("Nhap mot chuoi ki tu: ")
chuoi_max = ""
chuoi_tam = ""
ky_tu_truoc = ""

for ky_tu in chuoi_nhap:
    if ky_tu == ky_tu_truoc or ky_tu_truoc == "":
        chuoi_tam += ky_tu
    else:
        if len(chuoi_tam) > len(chuoi_max):
            chuoi_max = chuoi_tam
        chuoi_tam = ky_tu
    ky_tu_truoc = ky_tu

if len(chuoi_tam) > len(chuoi_max):
    chuoi_max = chuoi_tam

if chuoi_nhap != "":
    print("Chuoi con lap dai nhat:", chuoi_max)