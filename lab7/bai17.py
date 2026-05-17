d = {}

n = int(input("Nhập số sinh viên: "))

for i in range(n):
    ma_sv = input("Nhập mã sinh viên (6 ký tự): ")
    ten_sv = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm số: "))
    
    diem_lam_tron = round(diem)
    if diem_lam_tron > 10:
        diem_lam_tron = 10
    elif diem_lam_tron < 0:
        diem_lam_tron = 0
    
    d[ma_sv] = {"ten": ten_sv, "diem": diem_lam_tron}

print("\nThông tin sinh viên:")
for ma_sv in d:
    print("Mã: " + ma_sv + " - Tên: " + d[ma_sv]["ten"] + " - Điểm: " + str(d[ma_sv]["diem"]))
