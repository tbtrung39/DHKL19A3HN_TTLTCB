'''2. Viết chương trình nhập vào các hệ số a, b, c và
in ra nghiệm của phương trình bậc hai ax^2+bx+c=0 (giải và biện luận đầy đủ các trường hợp).'''

import math as m
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình bậc nhất", "nghiệm x= "-c/b)
else:
    delta = b**2 - 4*a*c
    if delta == 0:
        x = -b /(2*a)
        print("Phương trình có nghiệm kép x = ",x )
    elif delta < 0:
        print("Phương trình vô nghiệm")
    else:
        x1 = (-b + m.sqrt(delta)) / ( 2*a)
        x2 = (-b - m.sqrt(delta)) / ( 2*a)
        print("Phương trình của 2 nghiệm phân biệt là:", end="")
        print("x1= ",x1)
        print("x2= ",x2)    
    