def tim_max_de_quy(danh_sach):
    if len(danh_sach) == 1:
        return danh_sach[0]
    max_cua_phan_con_lai = tim_max_de_quy(danh_sach[1:])
    
    if danh_sach[0] > max_cua_phan_con_lai:
        return danh_sach[0]
    else:
        return max_cua_phan_con_lai

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
cac_so = [a, b, c]
so_lon_nhat = tim_max_de_quy(cac_so)
print(f"Số lớn nhất trong 3 số là: {so_lon_nhat}")