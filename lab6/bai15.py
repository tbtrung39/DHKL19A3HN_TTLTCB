danh_sach = []
while True:
    dong = input("Nhap ten, tuoi, diem (Nhap 'ngung' de thoi): ").strip()
    if dong == "ngung":
        break
    
    parts = dong.split(",")
    ten = parts[0].strip()
    tuoi = int(parts[1].strip())
    diem = int(parts[2].strip())
    danh_sach.append((ten, tuoi, diem))

danh_sach.sort(key = lambda x: (x[0], x[1], x[2]))
print(danh_sach)