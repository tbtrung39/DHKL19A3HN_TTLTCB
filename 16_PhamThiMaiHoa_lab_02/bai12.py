thang = int(input("Nhập tháng: "))

if thang in [1,3,5,7,8,10,12]:
    print("Có 31 ngày")
elif thang in [4,6,9,11]:
    print("Có 30 ngày")
elif thang == 2:
    print("Có 28 hoặc 29 ngày")
else:
    print("Tháng không hợp lệ")