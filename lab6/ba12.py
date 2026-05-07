so_du = 0
while True:
    dong = input("Nhap giao dich: ").strip()
    if dong == "ngung":
        break
    
    parts = dong.split()
    loai = parts[0]
    tien = int(parts[1])
    
    if loai == "D":
        so_du = so_du + tien
    elif loai == "W":
        so_du = so_du - tien

print(so_du)