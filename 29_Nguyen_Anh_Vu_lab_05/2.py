chuoi = input("Nhập một chuỗi: ")
ky_tu_dac_biet = ""
ky_tu_latinh = ""
ky_tu_so = ""
for i in chuoi:
    if(i.isalpha()):
        ky_tu_latinh += i
    elif(i.isdigit()):
        ky_tu_so += i
    else:
        ky_tu_dac_biet += i
print(f"Chuỗi ký tự dạng số có số ký tự là: {len(ky_tu_so)}, {ky_tu_so}")
print(f"Chuỗi ký tự dạng chữ có số ký tự là: {len(ky_tu_latinh)}, {ky_tu_latinh}")
print(f"Chuỗi ký tự đặc biệt có số ký tự là: {len(ky_tu_dac_biet)}, {(ky_tu_dac_biet).split(' ')}")
