chuoi = input("Nhap ma container: ").upper()
tong = 0
for i in range(len(chuoi)):
    ki_tu = chuoi[i]
    if ki_tu.isdigit():
        gia_tri = int(ki_tu)
    else:
        dem = ord(ki_tu) - ord('A') + 10
        while dem % 11 == 0:
            dem += 1
        gia_tri = dem
    tong += gia_tri * (2**i)
print("Kiem tra digit =", tong % 11)