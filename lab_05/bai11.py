s = input("Nhập chuỗi nhị phân: ")
kq = 0
for c in s:
    if c != '0' and c != '1':
        print("Không phải chuỗi nhị phân")
        break
    kq = kq * 2 + int(c)
else:
    print("Số thập phân:", kq)