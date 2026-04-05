a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))
if a == 0:
    x = -c/b
    print("Phương trình có nghiện duy nhất =",x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nhiệm")
    elif delta == 0:
        x = -b / 2*a
        print("Phương trình có nghiệm =",x)
    elif delta > 0:
        x1 = (-b + delta**0.5)/2*a
        x2 = (-b - delta**0.5)/2*a
        print("Phương trình có 2 nghiệm x1 = ",x1,"x2 =",x2)