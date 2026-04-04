chuoi_nhap = input("Nhap chuoi: ")
chuoi_da_loc = ""
la_hex = True
ky_tu_hex = "0123456789abcdefABCDEF"
for ky_tu in chuoi_nhap:
    if ky_tu in ky_tu_hex:
        chuoi_da_loc += ky_tu
    else:
        la_hex = False
if la_hex and chuoi_nhap != "":
    print("Chuoi da nhap khong hop le")
else:
    print("Chuoi khong phai he hex.")
if chuoi_da_loc != "":
    print(f"Chuoi hex con lai: {chuoi_da_loc}")
    gia_tri_thap_phan = 0
    for ky_tu in chuoi_da_loc:
        gia_tri = 0
        if ky_tu.isdigit():
            gia_tri = ord(ky_tu) - 48
        elif 'a' <= ky_tu <= 'f':
            gia_tri = ord(ky_tu) - 87
        elif 'A' <= ky_tu <= 'F':
            gia_tri = ord(ky_tu) - 55
        gia_tri_thap_phan = gia_tri_thap_phan * 16 + gia_tri
    print(f"Gia tri thap phan tuong ung: {gia_tri_thap_phan}")
else:
    print("Khong con ki tu hex nao sau khi loc" \
    "")