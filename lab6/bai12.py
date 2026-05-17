so_tien = 0

while True:
    giao_dich = input("Nhập giao dịch (D/W theo sau là số tiền, hoặc 'END' để kết thúc): ")
    
    if giao_dich == "END":
        break
    
    loai = giao_dich[0]
    so_tien_giao_dich = int(giao_dich[1:])
    
    if loai == "D":
        so_tien = so_tien + so_tien_giao_dich
    elif loai == "W":
        so_tien = so_tien - so_tien_giao_dich

print("Số tiền thực:", so_tien)
