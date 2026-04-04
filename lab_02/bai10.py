gio = int(input("nhập số giờ :"))
if gio <= 3:
    thanh_toan = gio * 100000
else:
    thanh_toan = 3* 100000 + (gio - 3) * 75000
giam= input("có thuê trong khung giờ từ 11h - 15h không?(y/n):")
if giam == 'y':
    giam = thanh_toan * 0.9
print(" số tiền cần phải thanh toán là :",thanh_toan)
