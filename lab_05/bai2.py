chuoi = input("Nhap mot chuoi: ")
ky_tu_dac_biet = ""
ky_tu_latinh = ""
ky_tu_so = ""
for i in chuoi:
    if(i.isalpha()):
        ky_tu_latinh += i
    elif(i.isdigit()):
        ky_tu_so += i
    else:
        ky_tu_dac_biet += i
print(f"Chuoi ki tu dang so co so ki tu la: {len(ky_tu_so)}, {ky_tu_so}")
print(f"Chuoi ki tu dang chu co so ki tu la: {len(ky_tu_latinh)}, {ky_tu_latinh}")
print(f"Chuoi ki tu dac biet co so ki tu la: {len(ky_tu_dac_biet)}, {(ky_tu_dac_biet).split(' ')}")