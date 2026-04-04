so_n = int(input("Nhap số tự nhien n: "))
if so_n == 0:
    chuoi_nhi_phan = "0"
else:
    chuoi_nhi_phan = ""
    tam = so_n
    while tam > 0:
        chuoi_nhi_phan = str(tam % 2) + chuoi_nhi_phan
        tam //= 2
print("Chuoi nhi phan tuong ung:", chuoi_nhi_phan)