kw = float(input("Nhập số KW điện tiêu thụ: "))

if kw < 0:
    print("Số KW điện không hợp lệ")
elif kw <= 100:
    tien = kw * 2000
    print("Tổng tiền điện phải trả là:", tien, "VND")
elif kw <= 200:
    tien = 100 * 2000 + (kw - 100) * 2500
    print("Tổng tiền điện phải trả là:", tien, "VND")
elif kw <= 300:
    tien = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
    print("Tổng tiền điện phải trả là:", tien, "VND")
else:
    tien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000
    print("Tổng tiền điện phải trả là:", tien, "VND")