thang = int(input("Nhập tháng: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print(31,"ngày")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print(30,"ngày")
elif thang == 2:
    print(28,"ngày")
else:
    print("Tháng không hợp lệ")