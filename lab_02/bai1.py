thang=int(input("Nhap thang: "))
if thang == 1 or thang==3 or thang ==5 or thang ==7 or thang==8 or thang == 10 or thang ==12:
    print("tháng ",thang, "có 31 ngày")
elif thang == 4 or thang ==6 or thang ==9 or thang == 11:
    print("thang", thang, "có 30 ngày")
elif thang ==2:
    print("tháng", thang, "có 28 ngày")
else:
    print("Tháng không hợp lệ, vui lòng nhập lại")