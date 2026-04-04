n = int(input("Nhập n: "))
if(n < 0):
    print("Nhập lại!")
else:
    s4 = 0
    s5 = 0
    s6 = 0
    for i in range(n+1):
        s4 += i**2
        s5 += (2*n + 1)**3
        s6 += (2*n)**4
    print(f"Giá trị của S4 là: {s4}")
    print(f"Giá trị của S5 là: {s5}")
    print(f"Giá trị của S6 là: {s6}")