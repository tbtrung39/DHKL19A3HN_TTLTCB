import math
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c:"))
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x = -c / b
        print("phuong trinh co mot nghiem duy nhat là: ",x)
    
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / 2*a
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("phuong trinh co 2 nghiem phan biet x1 = ",x1,", x2 = ",x2)