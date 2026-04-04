n = int(input("Nhập 1 số tự nhiên n :"))
so_ban_dau = n
if n == 0 :
    chuoi_nhi_phan = "0"
else:
    chuoi_nhi_phan = ""
    while n >0:
        du = n % 2
        chuoi_nhi_phan = str(du) + chuoi_nhi_phan
        n = n // 2
print(f"số{so_ban_dau} chuyển sang hệ nhị phân là :{chuoi_nhi_phan}")