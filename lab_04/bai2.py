n = int(input("Nhap n: "))
S = 0
i = 1
while i <= n :
    S +=  1 / (i*(i+1))
    i += 1
print("S= ",S)