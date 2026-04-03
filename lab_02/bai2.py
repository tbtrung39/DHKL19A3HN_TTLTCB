a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
if a ==0:
    if b == 0:
        if c ==0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -c / b
        print("Phuong trinh co nghiem duy nhat:", x)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co nghiem kep:", x)
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Phuong trinh co 2 nghiem phan biet:")
        print("x1 =", x1)
        print("x2 =", x2)


