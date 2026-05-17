def nam_nhuan(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
y = int(input("Nhap nam: "))
if nam_nhuan(y):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")