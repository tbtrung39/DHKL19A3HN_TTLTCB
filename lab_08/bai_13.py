def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def so_ngay_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return "Thang khong hop le"

# chuong trinh chinh
y = int(input("Nhap nam: "))
m = int(input("Nhap thang: "))

print("Nam nhuan:", nam_nhuan(y))
print("So ngay trong thang:", so_ngay_thang(m, y))