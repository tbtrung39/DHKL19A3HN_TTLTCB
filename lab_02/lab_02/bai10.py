bd = int(input("Gio bat dau: "))
kt = int(input("Gio ket thuc: "))
gio = kt - bd
tien = 0
if gio <= 3:
    tien = gio * 100000
else:
    tien = 3 * 100000
    tien += (gio - 3) * 75000
if 11 <= bd < 15:
    tien *= 0.9
print("Tien:", tien)