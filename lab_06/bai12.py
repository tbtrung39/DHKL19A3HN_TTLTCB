so_du = 0
while True:
    dong = input("Nhap giao dich (hoac Enter de dung): ")
    if dong == "":
        break
    loai, so_tien = dong.split()
    so_tien = int(so_tien)
    if loai == "D":
        so_du += so_tien
    elif loai == "W":
        so_du -= so_tien
print("So du cuoi:", so_du)