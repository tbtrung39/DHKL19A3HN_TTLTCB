a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
print(f"phương trình bậc 2: \nf(x) = {a}*x**2 + {b}*x + {c}")
delta = b**2 - 4*a*c
print("Giá trị của delta là:", delta)

if(delta < 0):
    print(f"Phương trình {a}*x**2 + {b}*x + {c} vô nghiệm!")
elif(delta == 0):
    print(f"Nghiệm của phương trình {a}*x**2 + {b}*x + {c} là:")
    print(f"x1 = x2 = -b/2a = {-b/2*a}")
else:
    print(f"Nghiệm của phương trình {a}*x**2 + {b}*x + {c} là:")
    print(f"x1 = (-b + delta**2)/2*a = {(-b + delta**2)/2*a},\nx2 = (-b - delta**2)/2*a = {(-b - delta**2)/2*a}")