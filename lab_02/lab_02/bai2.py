import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a == 0:
    if b == 0:
        print("Vo nghiem")
    else:
        print("Nghiemm:", -c/b)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        print("Nghiem kep:", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("x1 =", x1, ", x2 =", x2)