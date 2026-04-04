chuoi = input("Nhập mã container: ").upper()

tong = 0

for i in range(len(chuoi)):
    ky_tu = chuoi[i]
    if ky_tu.isdigit():
        gia_tri = int(ky_tu)
    else:
        dem = ord(ky_tu) - ord('A') + 10
        while dem % 11 == 0:
            dem += 1
        gia_tri = dem
    tong += gia_tri * (2**i)
print("Kiểm tra digit =", tong % 11)