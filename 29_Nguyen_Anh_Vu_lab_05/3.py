so_n = int(input("Nhập số tự nhiên n: "))
if so_n == 0:
    chuoi_nhi_phan = "0"
else:
    chuoi_nhi_phan = ""
    tam = so_n
    while tam > 0:
        chuoi_nhi_phan = str(tam % 2) + chuoi_nhi_phan
        tam //= 2
print("Chuỗi nhị phân tương ứng:", chuoi_nhi_phan)