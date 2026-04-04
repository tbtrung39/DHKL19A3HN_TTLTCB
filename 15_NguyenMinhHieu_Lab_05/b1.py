chuoi = input("Nhập chuỗi ký tự(gồm cả chữ và số): ")
chuoi_ky_tu = ""
chuoi_so = ""
for i in chuoi:
    if(i.isdigit()):
        chuoi_so += i
    else:
        chuoi_ky_tu += i
print(f"Chuỗi ký tự dạng số có số ký tự là: {chuoi_so}")
print(f"Chuỗi ký tự dạng ký tự có số ký tự là: {chuoi_ky_tu}")