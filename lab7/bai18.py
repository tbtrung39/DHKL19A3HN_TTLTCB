tu_dien_thi = {}
while True:
    sbd = input("Nhap SBD (ngung de thoat): ")
    if sbd == "ngung":
        break
    ten = input("Nhap ho ten: ")
    diem = float(input("Nhap diem thi: "))
    
    if sbd in tu_dien_thi:
        print(f"SV trung SBD! Ten: {ten}, Diem: {diem}")
    else:
        tu_dien_thi[sbd] = {"ten": ten, "diem": diem}

print(tu_dien_thi)