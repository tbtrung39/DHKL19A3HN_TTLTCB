so_du = 0

while True:
    try:
        s = input()
        loai, tien = s.split()
        tien = int(tien)

        if loai == "D":
            so_du += tien
        elif loai == "W":
            so_du -= tien
    except:
        break

print(so_du)