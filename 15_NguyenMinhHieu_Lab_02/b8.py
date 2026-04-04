tnct = int(input("Nhập thời gian tnct: "))
if(tnct < 12):
    luong = 2.34 * 1350000
    print(f"Lương của nhân viên với thời gian TNCT dài {tnct} tháng là: {luong}")
elif(tnct >= 12 and tnct < 36):
    luong = 3.33 * 1350000
    print(f"Lương của nhân viên với thời gian TNCT dài {tnct} tháng là: {luong}")
elif(tnct >= 36 and tnct < 60):
    luong = 3.66 * 1350000
    print(f"Lương của nhân viên với thời gian TNCT dài {tnct} tháng là: {luong}")
else:
    luong = 3.99 * 1350000
    print(f"Lương của nhân viên với thời gian TNCT dài {tnct} tháng là: {luong}")