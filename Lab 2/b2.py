import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Vo so nghiem")
        if c != 0:
            print("Vo nghiem")
    if b != 0:
        print("x =", -c/b)

if a != 0:
    d = b*b - 4*a*c
    
    if d > 0:
        print("x1 =", (-b + math.sqrt(d))/(2*a))
        print("x2 =", (-b - math.sqrt(d))/(2*a))
        
    if d == 0:
        print("x =", -b/(2*a))
        
    if d < 0:
        print("Vo nghiem")