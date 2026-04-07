n = int(input("Nhập một số tự nhiên n: "))
if n == 0:
    chuoi_nhi_phan = "0"
else:
    chuoi_nhi_phan = ""
    while n > 0:
        phan_du = n % 2
        chuoi_nhi_phan = str(phan_du) + chuoi_nhi_phan 
        n = n // 2
print(f"Chuỗi nhị phân: {chuoi_nhi_phan}")