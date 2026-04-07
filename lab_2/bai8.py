n = int(input("nhap tham nien cong tac(thang): "))
luong_cb = 1350000
if n < 12:
    luong = 2.34 * luong_cb
elif 12<= n < 36:
    luong = 3.33 * luong_cb
elif 36 <= n < 60:
    luong = 3.66 * luong_cb
elif n >= 60:
    luong = 3.99 * luong_cb
print("luong :",luong,"dong")