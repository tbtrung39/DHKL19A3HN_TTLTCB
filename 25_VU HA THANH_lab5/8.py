Str = "Hoc nua hoc mai, hoc tap la tot. Hoc di doi voi hanh."
tu_can_tim = input("Nhập từ cần tìm: ")
danh_sach_tu = Str.split()
dem = 0
for tu in danh_sach_tu:
    tu = tu.strip(",.") 
    if tu.lower() == tu_can_tim.lower():
        dem = dem + 1
print("Từ '", tu_can_tim, "' xuất hiện", dem, "lần.")