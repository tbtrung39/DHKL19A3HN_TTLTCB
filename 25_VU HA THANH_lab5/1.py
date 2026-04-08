chuoi = input("Nhập vào một chuỗi: ")

so_luong_so = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        so_luong_so += 1 
print("Số lượng ký tự là số trong chuỗi là:", so_luong_so)